import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import plotly.express as px
from PIL import Image
from io import BytesIO
import requests

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

# ============ LOAD AND PROCESS DATA ============

@st.cache_data
def load_data():
    """Load and prepare the streaming titles dataset"""
    try:
        # Load the correct CSV file
        df = pd.read_csv('expanded_streaming_titles_2022_2026.csv')
        
        # Display loading info
        st.info(f"✅ Loaded {len(df):,} titles from dataset")
        
        # Sample 5000 titles to avoid memory issues
        df_sample = df.sample(n=min(5000, len(df)), random_state=42).reset_index(drop=True)
        return df_sample
    except FileNotFoundError:
        st.error("❌ CSV file not found! Make sure 'expanded_streaming_titles_2022_2026.csv' is in the same folder as app.py")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()

@st.cache_data
def compute_similarity(df_processed):
    """Compute TF-IDF similarity matrix"""
    try:
        # Combine genres and description for features
        df_processed['features'] = (
            df_processed['listed_in'].fillna('') + ' ' + 
            df_processed['description'].fillna('')
        ).str.lower()
        
        # Get stopwords
        stop_words = stopwords.words('english')
        
        # Create TF-IDF vectorizer
        tfidf = TfidfVectorizer(
            stop_words=stop_words, 
            max_features=3000, 
            ngram_range=(1,2)
        )
        
        # Fit and transform
        tfidf_matrix = tfidf.fit_transform(df_processed['features'])
        
        # Compute cosine similarity
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        return cosine_sim
    except Exception as e:
        st.error(f"❌ Error computing similarity: {str(e)}")
        st.stop()

def get_poster_image(poster_url, title):
    """Fetch poster image from URL with fallback"""
    try:
        if pd.isna(poster_url) or poster_url == '':
            return None
        
        response = requests.get(poster_url, timeout=5)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        return None
    except:
        return None

def display_recommendation_cards(recs):
    """Display recommendations as beautiful poster grid (6 columns)"""
    st.subheader("📺 Top Recommendations")
    
    # Display in grid format (6 columns per row - Netflix style)
    cols_per_row = 6
    
    for idx in range(0, len(recs), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for col_idx, col in enumerate(cols):
            if idx + col_idx < len(recs):
                rec = recs.iloc[idx + col_idx]
                
                with col:
                    # Create card container
                    with st.container():
                        # Display poster
                        poster_image = get_poster_image(rec.get('poster_url'), rec['title'])
                        
                        if poster_image:
                            st.image(poster_image, use_container_width=True)
                        else:
                            # Fallback: colored placeholder with emoji
                            st.markdown(f"""
                                <div style="
                                    width: 100%;
                                    aspect-ratio: 2/3;
                                    background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                    border-radius: 8px;
                                    font-size: 36px;
                                    color: white;
                                ">
                                    {'🎬' if rec['type'] == 'Movie' else '📺'}
                                </div>
                            """, unsafe_allow_html=True)
                        
                        # Title (truncated for compact display)
                        title_text = rec['title']
                        if len(title_text) > 25:
                            title_text = title_text[:22] + "..."
                        st.markdown(f"**{title_text}**", help=rec['title'])
                        
                        # Type and Year (compact)
                        content_type = rec['type']
                        year = rec.get('release_year', 'N/A')
                        st.caption(f"🎭 {content_type} • {year}")
                        
                        # Genres (compact)
                        genres = str(rec.get('listed_in', 'N/A'))
                        if len(genres) > 35:
                            genres = genres[:32] + "..."
                        st.caption(f"📁 {genres}")
                        
                        # Rating
                        rating = rec.get('rating', 'N/A')
                        st.caption(f"⭐ {rating}")
                        
                        # Similarity Score (as a smaller metric)
                        similarity = rec.get('Similarity Score', 0)
                        st.metric("Match", f"{similarity:.0%}", label_visibility="collapsed")
                        
                        # Platform availability (compact icons)
                        platforms = []
                        if rec.get('Amazon Prime') == 1:
                            platforms.append("🔴")
                        if rec.get('Netflix') == 1:
                            platforms.append("🔴")
                        if rec.get('Disney Plus') == 1:
                            platforms.append("🔵")
                        if rec.get('Hulu') == 1:
                            platforms.append("🟢")
                        
                        if platforms:
                            st.caption(f"Platforms: {' '.join(platforms)}")

# Load data
df_processed = load_data()
cosine_sim = compute_similarity(df_processed)

def recommend(title, platform=None, top_k=10):
    """Get recommendations with error handling"""
    try:
        # Find matching title
        matching = df_processed[df_processed['title'].str.contains(title, case=False, na=False)]
        
        if matching.empty:
            return pd.DataFrame({
                "Error": [f"Title '{title}' not found. Try another title."]
            })
        
        # Get the first matching title index
        local_idx = matching.index[0]
        
        if local_idx >= len(cosine_sim):
            return pd.DataFrame({
                "Error": ["Index error - restart app"]
            })
        
        # Get similarity scores
        sim_scores = sorted(
            list(enumerate(cosine_sim[local_idx])), 
            key=lambda x: x[1], 
            reverse=True
        )[1:top_k+1]
        
        # Get recommendation indices
        rec_indices = [i[0] for i in sim_scores]
        
        # Build recommendation dataframe
        rec_df = df_processed.iloc[rec_indices][
            ['title', 'type', 'rating', 'listed_in', 'release_year',
             'Amazon Prime', 'Disney Plus', 'Hulu', 'Netflix', 'poster_url',
             'description', 'director', 'cast']
        ].copy()
        
        rec_df.insert(0, 'Similarity Score', [s[1] for s in sim_scores])
        
        # Filter by platform if specified
        if platform and platform != 'All':
            rec_df = rec_df[rec_df[platform] == 1]
        
        return rec_df.head(top_k)
    except Exception as e:
        return pd.DataFrame({"Error": [f"Error: {str(e)}"]})

# ============ PAGE CONFIG & STYLING ============

st.set_page_config(
    page_title="StreamVault - OTT Recommendation Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .recommendation-card {
        background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
        color: white;
    }
    
    .metric-box {
        background: linear-gradient(135deg, #E94560 0%, #FF006E 100%);
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    
    /* Make columns more compact */
    [data-testid="column"] {
        min-width: calc(100% / 6) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============ MAIN TITLE ============

st.title("🎬 StreamVault - OTT Recommendation Engine")
st.subheader("Discover your next favorite show or movie with AI-powered recommendations!")

# ============ SIDEBAR STATS ============

with st.sidebar:
    st.header("📊 Dataset Statistics")
    
    # Platform counts
    platforms = ['Amazon Prime', 'Disney Plus', 'Hulu', 'Netflix']
    counts = [int(df_processed[p].sum()) for p in platforms]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Titles", f"{len(df_processed):,}")
    with col2:
        st.metric("Unique Genres", df_processed['listed_in'].nunique())
    
    st.markdown("---")
    
    # Platform pie chart
    fig_pie = px.pie(
        values=counts,
        names=platforms,
        title="Titles per Platform",
        color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Top genres
    st.markdown("---")
    genre_counts = df_processed['listed_in'].str.split(', ', expand=True).stack().value_counts().head(8)
    fig_bar = px.bar(
        x=genre_counts.values,
        y=genre_counts.index,
        orientation='h',
        title="Top 8 Genres",
        labels={'x': 'Count', 'y': 'Genre'},
        color_discrete_sequence=['#FF6B6B']
    )
    fig_bar.update_layout(height=400)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.caption("📈 Built with TF-IDF content-based filtering")

# ============ MAIN RECOMMENDATION SECTION ============

st.markdown("---")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    title = st.text_input(
        "🔍 Enter a movie or TV show title:",
        "Inception",
        help="Type any title from the dataset"
    )

with col2:
    platform = st.selectbox(
        "Filter by Platform:",
        ['All', 'Amazon Prime', 'Disney Plus', 'Hulu', 'Netflix'],
        help="Select platform to filter results"
    )

with col3:
    top_k = st.slider("Show Top:", 6, 30, 18)

# ============ RECOMMENDATION RESULTS ============

if st.button("🎯 Get Recommendations", type="primary", use_container_width=True):
    with st.spinner("🔄 Computing similar titles and fetching posters..."):
        recs = recommend(title, platform, top_k)
        
        if 'Error' in recs.columns:
            st.error(f"❌ {recs['Error'].iloc[0]}")
            st.info("Sample titles: " + ", ".join(df_processed['title'].head(5).tolist()))
        else:
            st.success(f"✅ Found {len(recs)} recommendations!")
            
            # Display poster cards in 6-column grid
            display_recommendation_cards(recs)
            
            # Show table view option
            with st.expander("📊 View as Table"):
                display_df = recs[[
                    'title', 'type', 'rating', 'listed_in', 'Similarity Score'
                ]].copy()
                display_df['Similarity Score'] = display_df['Similarity Score'].apply(lambda x: f"{x:.1%}")
                st.dataframe(display_df, use_container_width=True, hide_index=True)
            
            # Genre distribution
            st.subheader("📊 Genre Distribution in Recommendations")
            rec_genres = recs['listed_in'].str.split(', ', expand=True).stack().value_counts().head(6)
            fig_genre = px.bar(
                x=rec_genres.index,
                y=rec_genres.values,
                title="Most Common Genres in Recommendations",
                labels={'x': 'Genre', 'y': 'Count'},
                color_discrete_sequence=['#FF6B6B']
            )
            st.plotly_chart(fig_genre, use_container_width=True)
            
            # Platform availability
            st.subheader("🌐 Platform Availability")
            platform_cols = ['Amazon Prime', 'Disney Plus', 'Hulu', 'Netflix']
            platform_avail = [int((recs[col] == 1).sum()) for col in platform_cols]
            fig_platform = px.bar(
                x=platform_cols,
                y=platform_avail,
                title="Available on Platforms",
                labels={'x': 'Platform', 'y': 'Count'},
                color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
            )
            st.plotly_chart(fig_platform, use_container_width=True)
            
            # Download CSV
            csv = recs[[
                'title', 'type', 'rating', 'listed_in', 'release_year', 
                'Similarity Score', 'Amazon Prime', 'Netflix', 'Disney Plus', 'Hulu'
            ]].to_csv(index=False)
            st.download_button(
                "📥 Download Results as CSV",
                csv,
                f"recommendations_{title.replace(' ', '_')}.csv",
                "text/csv"
            )

# ============ FOOTER ============

st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.caption("🛠️ Built with Streamlit")

with col_footer2:
    st.caption(f"📊 {len(df_processed):,} sampled titles dataset")

with col_footer3:
    st.caption("🤖 TF-IDF similarity engine with poster display")
