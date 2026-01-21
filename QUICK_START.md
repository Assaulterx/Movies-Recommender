# 🚀 StreamVault - Quick Start Guide

Get StreamVault up and running in 4 simple steps!

---

## Installation (< 2 minutes)

### Step 1: Install Python Packages
```bash
pip install -r requirements.txt
```

**What this does**: Installs Streamlit, Pandas, scikit-learn, Plotly, Pillow, and Requests

### Step 2: Run the App
```bash
streamlit run app_updated.py
```

**What this does**: Starts the Streamlit server

### Step 3: Open Browser
The app automatically opens at: `http://localhost:8501`

If not, open your browser and go to that URL.

### Step 4: Start Exploring!
Search for your favorite movie or show!

---

## Quick Feature Overview

### 🔍 Search & Recommendations
1. Enter a movie/show name (e.g., "Breaking Bad")
2. Adjust number of recommendations (5-20)
3. Filter by platform (Optional)
4. See beautiful recommendations with posters!

### 📊 Analytics
Click the "📈 Analytics" tab to see:
- Platform distribution
- Top genres
- Content type breakdown

### 🎯 Explore
Click the "🎯 Explore" tab to:
- Browse by platform
- Browse by genre
- Browse by type
- Discover random titles

---

## What You Get

✨ **Beautiful OTT Interface**
- Dark theme like Netflix/Prime
- Pink/purple gradients
- Smooth animations

📺 **Smart Poster Display**
- Real TMDB poster images
- Custom emojis as fallback
- Error handling

🔍 **Powerful Recommendations**
- TF-IDF algorithm
- Cosine similarity matching
- Platform filtering

📊 **Analytics Dashboard**
- Charts and statistics
- Quick insights
- Data export

---

## Before & After

### BEFORE (Original app.py)
❌ Simple Streamlit default interface
❌ No poster images
❌ Basic table layout
❌ Light color scheme
❌ No animations

### AFTER (StreamVault)
✅ Professional OTT interface (like Netflix/Prime)
✅ Beautiful poster display with emojis
✅ Stunning 5-column grid layout
✅ Dark theme with gradients
✅ Smooth animations and effects
✅ Glass morphism cards
✅ Analytics dashboard

---

## Search Examples

Try searching for:
- "Breaking Bad" → Gets TV show recommendations
- "Inception" → Gets movie recommendations
- "The Office" → Gets comedy recommendations
- "Dune" → Gets sci-fi recommendations

---

## Troubleshooting

**"Module not found" error?**
```bash
pip install -r requirements.txt
```

**App won't start?**
- Make sure you're in the correct directory
- Make sure CSV file exists in same folder
- Try: `streamlit run app_updated.py --logger.level=debug`

**Posters not showing?**
- This is normal - the app shows emoji if poster URL is unavailable
- No action needed!

**No search results?**
- Try searching for a partial name
- Try "All Platforms" filter
- Try a different show/movie

---

## Customization Tips

### Change Colors
Edit the CSS in `app_updated.py` (around line 40):
```python
# Change #E94560 and #FF006E to your colors
```

### Change Grid Columns
Edit in `app_updated.py` (around line 350):
```python
cols_per_row = 5  # Change to 4, 6, etc.
```

### Change Emoji Fallbacks
Edit in `app_updated.py` (around line 130):
```python
emoji_map = {
    'MOVIE': '🎬',      # Change emoji here
    'TV SHOW': '📺',    # Change emoji here
}
```

---

## Pro Tips 💡

1. **Search smartly**: Partial matches work! "Breaking" finds "Breaking Bad"
2. **Use filters**: Filter by platform to narrow results
3. **Check analytics**: See trending genres and platforms
4. **Export data**: Download CSV of all titles
5. **Explore randomly**: Discover new shows you might like

---

## Next Steps

- Read **README.md** for detailed documentation
- Check **DESIGN_GUIDE.md** for design customization
- See **CODE_CHANGES.md** for technical details

---

## File Checklist

Before running, make sure you have:

- ✅ `app_updated.py` (Main app)
- ✅ `requirements.txt` (Dependencies)
- ✅ `expanded_streaming_titles_2022_2026.csv` (Data)
- ✅ `config.toml` (Streamlit config - optional)

---

## One-Liner Commands

**Quick install & run:**
```bash
pip install -r requirements.txt && streamlit run app_updated.py
```

**Run on custom port:**
```bash
streamlit run app_updated.py --server.port 8502
```

**Run in debug mode:**
```bash
streamlit run app_updated.py --logger.level=debug
```

---

## Features at a Glance

| Feature | Status |
|---------|--------|
| Search Recommendations | ✅ Active |
| Poster Display | ✅ Active |
| Platform Filtering | ✅ Active |
| Analytics Dashboard | ✅ Active |
| Explore Tab | ✅ Active |
| Responsive Design | ✅ Active |
| Dark Theme | ✅ Active |
| CSV Export | ✅ Active |

---

## Performance

- **Data Load**: ~1 second (first time), instant after caching
- **Search**: ~0.5 seconds
- **Poster Load**: ~1-2 seconds (first time)
- **Subsequent Searches**: Instant (cached)

---

## Questions?

1. **Won't start?** → Check README.md Troubleshooting
2. **Want to customize?** → See DESIGN_GUIDE.md
3. **Want technical details?** → See CODE_CHANGES.md
4. **Need help with data?** → Check SUMMARY.md

---

Happy Streaming! 🎬✨

**Enjoy your new StreamVault platform!**
