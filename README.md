# 🎬 StreamVault - OTT Recommendation Platform

## Complete Documentation

### Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage Guide](#usage-guide)
5. [How It Works](#how-it-works)
6. [File Structure](#file-structure)
7. [Troubleshooting](#troubleshooting)
8. [Customization](#customization)

---

## Overview

**StreamVault** is a modern, professional OTT (Over-The-Top) streaming recommendation platform built with Streamlit. It uses machine learning (TF-IDF algorithm) to recommend movies and TV shows based on user input, with a beautiful Netflix/Prime Video-style interface.

### Key Highlights
- 🎨 **Modern Dark Theme**: Professional OTT-style interface
- 🔍 **Smart Recommendations**: TF-IDF similarity algorithm
- 📺 **Poster Display**: Real TMDB posters with emoji fallbacks
- 📊 **Analytics Dashboard**: Comprehensive statistics
- 🌍 **Platform Filtering**: Filter by streaming service
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- ⚡ **Fast Performance**: Cached data loading and processing

---

## Features

### 🔍 Recommendation Engine
- **TF-IDF Vectorization**: Analyzes title, description, and genre
- **Cosine Similarity**: Finds titles most similar to your search
- **Flexible Filtering**: Filter results by platform (Netflix, Prime, Disney+, Hulu)
- **Adjustable Results**: Get 5-20 recommendations

### 🎨 User Interface
- **Dark Theme**: Reduces eye strain, looks professional
- **Gradient Effects**: Pink/purple (#E94560 → #FF006E) color scheme
- **Glass Morphism**: Glassmorphic cards with backdrop blur
- **Smooth Animations**: Hover effects and transitions
- **Responsive Layout**: 5-column grid (desktop), adapts to mobile

### 📺 Poster Display System
- **TMDB Integration**: Loads real poster images from URLs
- **Smart Fallback**: Shows custom emoji when posters unavailable
  - 🎬 for Movies
  - 📺 for TV Shows
  - 🎭 as backup
- **Error Handling**: Gracefully handles network errors
- **Image Caching**: Fast loading on repeated requests

### 📊 Analytics Dashboard
- **Platform Distribution**: Pie chart of titles by platform
- **Top Genres**: Bar chart of most common genres
- **Content Type Breakdown**: Movies vs TV shows distribution
- **Quick Stats**: Total titles, genres, platforms, and date range

### 🎯 Explore Features
- **Browse by Platform**: See all titles on Netflix, Prime, etc.
- **Browse by Genre**: Filter by specific genre
- **Browse by Type**: Separate movies and TV shows
- **Random Selection**: Discover random titles

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Setup

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**
   ```bash
   python -c "import streamlit; print('✅ Streamlit installed')"
   ```

3. **Run the Application**
   ```bash
   streamlit run app_updated.py
   ```

4. **Open in Browser**
   The app will automatically open at: `http://localhost:8501`

### Dependencies
- **streamlit** (1.28.1): Web framework
- **pandas** (2.1.3): Data manipulation
- **scikit-learn** (1.3.2): TF-IDF vectorization
- **plotly** (5.18.0): Interactive charts
- **numpy** (1.24.3): Numerical operations
- **Pillow** (10.1.0): Image processing
- **requests** (2.31.0): HTTP requests for posters

---

## Usage Guide

### Getting Started

1. **Search for a Title**
   - Enter a movie or TV show name in the "Search for a title" field
   - Examples: "Breaking Bad", "Inception", "The Office"

2. **Adjust Recommendations**
   - Use the "Number of recommendations" slider (5-20 titles)
   - Filter by platform using the dropdown

3. **View Results**
   - Results display in a beautiful 5-column grid
   - Each card shows:
     - Poster image (or emoji if unavailable)
     - Title
     - Type (Movie/TV Show)
     - Platform
     - Genre
     - Similarity score (%)

### Tabs Explained

#### 🔍 Recommendations Tab
- Main search interface
- Shows recommended titles with posters
- Displays similarity percentage
- Featured random titles when no search query

#### 📈 Analytics Tab
- **Platform Distribution**: Pie chart showing titles per platform
- **Top Genres**: Bar chart of most popular genres
- **Content Type**: Breakdown of movies vs TV shows
- **Quick Stats**: Overview of dataset size

#### 🎯 Explore Tab
- **Browse by Platform**: See all titles on specific service
- **Browse by Genre**: Filter by genre (Drama, Action, etc.)
- **Browse by Type**: Separate movies and shows
- **Random Selection**: Discover new titles randomly

### Sidebar Options
- **Search Input**: Enter title to search
- **Number of Recommendations**: 5-20 slider
- **Platform Filter**: "All Platforms" or specific service
- **Quick Stats**: Display key metrics
- **Export Data**: Download CSV of current data

---

## How It Works

### Algorithm: TF-IDF + Cosine Similarity

1. **Data Preparation**
   - Combine title, description, and genre into single text
   - Convert to lowercase for consistency
   - Remove null values

2. **TF-IDF Vectorization**
   - Convert text to numerical vectors
   - TF-IDF (Term Frequency-Inverse Document Frequency) weights words
   - Common words get lower weight, unique words get higher weight
   - Results in 500-dimensional vectors

3. **Similarity Calculation**
   - Compute cosine similarity between search term and all titles
   - Cosine similarity ranges from 0 (no similarity) to 1 (identical)
   - Sort by similarity score in descending order

4. **Filtering & Ranking**
   - Filter by platform if specified
   - Select top N recommendations (5-20)
   - Display with posters and metadata

### Example Flow

```
User Input: "Breaking Bad"
    ↓
TF-IDF: Create vector representation
    ↓
Similarity: Calculate similarity to all 6000+ titles
    ↓
Filter: Show only Netflix/Prime (if filtered)
    ↓
Display: Top 10 similar titles with posters
```

---

## File Structure

```
project/
├── app_updated.py                          # Main application file
├── requirements.txt                        # Python dependencies
├── config.toml                             # Streamlit configuration
├── expanded_streaming_titles_2022_2026.csv # Data file
├── README.md                               # This file
├── QUICK_START.md                          # Quick start guide
├── SUMMARY.md                              # What's new summary
├── CODE_CHANGES.md                         # Technical changes
└── DESIGN_GUIDE.md                         # Design specifications
```

### CSV File Format

The `expanded_streaming_titles_2022_2026.csv` should contain:

| Column | Type | Description |
|--------|------|-------------|
| title | string | Movie/show name |
| type | string | "MOVIE" or "TV SHOW" |
| description | string | Plot summary |
| genre | string | Comma-separated genres |
| platform | string | Streaming service(s) |
| posterurl | string | TMDB poster image URL |

---

## Troubleshooting

### Issue: "CSV file not found"
**Solution**: Ensure `expanded_streaming_titles_2022_2026.csv` is in the same directory as `app_updated.py`

### Issue: "No module named 'streamlit'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Posters not loading
**Solution**: This is normal - the app falls back to emoji. Check:
1. CSV posterurl column has valid TMDB URLs
2. Internet connection is working
3. TMDB servers are accessible (not blocked)

### Issue: Slow performance with large datasets
**Solution**: 
- Data is cached after first load
- Subsequent searches are instant
- If still slow, reduce number of recommendations

### Issue: "No recommendations found"
**Causes**:
- Exact title not in database (try partial match)
- Platform filter too restrictive
- Try different search term

**Solutions**:
- Search for partial titles (e.g., "Breaking" instead of "Breaking Bad")
- Use "All Platforms" filter
- Try similar titles

### Issue: Port 8501 already in use
**Solution**: Use different port
```bash
streamlit run app_updated.py --server.port 8502
```

---

## Customization

### Change Color Scheme

In `app_updated.py`, find the CSS section and modify colors:

```python
# Current colors (Pink/Magenta theme)
Primary: #E94560 → #FF006E
Secondary: #667EEA → #764BA2
Background: #0F3460 → #1A1A2E

# To change, update these values:
# Line ~40-50 in the CSS block
```

### Change Number of Columns

In `app_updated.py`, find the grid display:

```python
# Current: 5 columns for desktop
cols_per_row = 5

# Change to 4, 6, or any number you want
cols_per_row = 4  # Now displays 4 columns
```

### Modify Emoji Fallbacks

In `app_updated.py`, find the emoji mapping:

```python
emoji_map = {
    'MOVIE': '🎬',      # Change to any emoji
    'TV SHOW': '📺',    # Change to any emoji
    'SHOW': '📺'
}
```

### Add Custom CSS

Add to the CSS block:

```python
/* Your custom styles */
.my-custom-class {
    color: #YOUR_COLOR;
    /* More CSS */
}
```

---

## Advanced Features

### Caching

The app uses Streamlit caching for performance:

```python
@st.cache_resource
def load_data():
    # Loads CSV once, reuses on subsequent runs
    df = pd.read_csv('expanded_streaming_titles_2022_2026.csv')
    return df
```

### Error Handling

Robust error handling for:
- Missing CSV files
- Invalid URLs
- Network timeouts (2-second timeout on poster requests)
- Empty search results
- Invalid data format

### Responsive Design

Automatic layout adjustment:
- **Desktop** (1920px+): 5 columns
- **Tablet** (768-1919px): 3-4 columns
- **Mobile** (<768px): 2 columns

---

## Performance Tips

1. **First Run**: App caches data after initial load
2. **Search**: Faster after first search (TF-IDF cached)
3. **Posters**: Images cached after first load
4. **Analytics**: Charts built once and cached

---

## Browser Compatibility

✅ **Fully Supported**:
- Chrome/Chromium
- Firefox
- Safari
- Edge

✅ **Responsive**: Works on mobile and tablet

---

## Security Notes

- No data is sent to external servers (except TMDB poster requests)
- All processing happens locally
- Safe file handling
- Input sanitization for search queries

---

## Future Enhancements

Potential features for v2.0:
- User rating/review system
- Watchlist functionality
- Similar users recommendations
- Genre-specific algorithms
- Release date filtering
- Rating/IMDb score filtering
- Multi-language support
- Dark/Light theme toggle

---

## Support & Feedback

For issues or feature requests, refer to:
- **QUICK_START.md**: Quick setup help
- **CODE_CHANGES.md**: Technical details
- **DESIGN_GUIDE.md**: Design customization

---

## License

This project is open-source and available for educational and commercial use.

---

## Credits

- Built with **Streamlit**
- Data from **Expanded Streaming Titles Dataset**
- Posters from **TMDB**
- Machine Learning: **scikit-learn**
- Visualizations: **Plotly**

---

**Happy Streaming! 🍿✨**
