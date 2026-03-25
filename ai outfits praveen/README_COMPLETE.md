# AI Outfit Recommendation System

## Overview
This project is a Python-based AI-powered outfit recommendation system with a modern Streamlit web interface. It analyzes a user's uploaded photo, detects features (gender, skin tone, face shape, body structure), and recommends personalized outfits (traditional, western, or casual) with matching Amazon product suggestions and styling tips. Users can override gender, and the UI is styled for clarity and engagement.

## Features
- **Image Upload & Analysis:** Upload a photo for AI-based feature extraction (face, skin, body type, gender).
- **Outfit Recommendation:** Personalized suggestions for traditional, western, or casual wear, tailored to gender and detected features.
- **Amazon Picks:** Curated product links for each outfit type and gender.
- **Styling Videos:** YouTube search links for how to style each outfit type and gender.
- **Modern UI:** Wide, visually appealing Streamlit interface with tabs, cards, and color highlights.
- **Gender Override:** User can manually select gender for recommendations.
- **No Data Storage:** All analysis is local; images are not stored or shared.

## Project Structure
```
c:\Users\msi\ai outfits\
│   app.py                  # Main Streamlit app
│   README_COMPLETE.md      # Project documentation (this file)
└───src
    │   image_analysis.py       # ImageAnalyzer: feature extraction from photos
    │   outfit_recommender.py   # OutfitRecommender: rule-based outfit logic
    │   amazon_suggestions.py   # AmazonSuggestions: product links by type/gender
    │   constants.py            # Outfit/style/color mappings
    │   outfit_visualizer.py    # (Legacy) Outfit mockup generator (not used)
```

## How It Works
1. **User uploads a photo** (JPG/PNG, clear face/upper body).
2. **AI analyzes the image** for gender, skin tone, face shape, and body structure.
3. **User selects outfit type** (Traditional, Western, Casual) and can override gender.
4. **Personalized recommendations** are generated:
   - Outfit styles, colors, accessories, and tips.
   - Amazon product suggestions for the chosen type/gender.
   - YouTube link for styling tips (based on type/gender).
5. **Results are shown in tabs:**
   - Analysis, Recommendations, Amazon Picks.

## Key Files
- **app.py:**
  - Streamlit UI, session state, tab logic, gender override, and all user interaction.
  - Integrates all modules and displays results.
- **src/image_analysis.py:**
  - `ImageAnalyzer` class: extracts features from uploaded images.
- **src/outfit_recommender.py:**
  - `OutfitRecommender` class: rule-based logic for outfit, color, and accessory selection, with gender-specific rules.
- **src/amazon_suggestions.py:**
  - `AmazonSuggestions` class: returns Amazon product links for each outfit type/gender.
- **src/constants.py:**
  - Contains mappings for outfit types, color palettes, and style rules.

## How to Run
1. Open a new PowerShell terminal.
2. Navigate to the project directory:
   ```
   cd "C:\Users\msi\ai outfits"
   ```
3. Start the Streamlit app:
   ```
   streamlit run app.py --logger.level=error
   ```
4. Open [http://localhost:8501](http://localhost:8501) in your browser.

## Customization
- **Add/Change Amazon links:** Edit `src/amazon_suggestions.py`.
- **Change style rules:** Edit `src/outfit_recommender.py` and `src/constants.py`.
- **Update YouTube links:** Edit the `youtube_links` dictionary in `app.py` (Recommendations tab section).

## YouTube Styling Links
- Traditional Female: https://www.youtube.com/results?search_query=how+to+style+traditional+female
- Traditional Male: https://www.youtube.com/results?search_query=how+to+style+traditional+male
- Western Female: https://www.youtube.com/results?search_query=how+to+style+western+female
- Western Male: https://www.youtube.com/results?search_query=how+to+style+western+male
- Casual Female: https://www.youtube.com/results?search_query=how+to+style+casual+female
- Casual Male: https://www.youtube.com/results?search_query=how+to+style+casual+male

## Notes
- The app does not perform real virtual try-on (no garment transfer on user photo).
- All processing is local; no images are uploaded to a server.
- For advanced try-on, see research models like VITON/CP-VTON (not included).

## Requirements
- Python 3.8+
- Streamlit
- Pillow
- OpenCV
- NumPy

Install requirements with:
```
pip install streamlit pillow opencv-python numpy
```

## Credits
- Developed with GitHub Copilot and user collaboration.
- Outfit logic and UI by user requirements.
- Amazon and YouTube links are for demonstration only.
