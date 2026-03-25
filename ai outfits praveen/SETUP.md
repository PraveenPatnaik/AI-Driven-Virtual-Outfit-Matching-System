"""
Setup Guide for AI Outfit Recommendation System
Quick start instructions for Windows, macOS, and Linux
"""

# ============================================================================
# INSTALLATION GUIDE
# ============================================================================

## WINDOWS USERS

1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   cd "C:\Users\msi\ai outfits"

3. Create virtual environment:
   python -m venv venv

4. Activate virtual environment:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the application:
   streamlit run app.py

The app will open at: http://localhost:8501


## macOS / LINUX USERS

1. Open Terminal
2. Navigate to the project directory:
   cd ~/ai\ outfits
   (or wherever you saved it)

3. Create virtual environment:
   python3 -m venv venv

4. Activate virtual environment:
   source venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the application:
   streamlit run app.py

The app will open at: http://localhost:8501


## TROUBLESHOOTING INSTALLATION

### Issue: Python not found
- Ensure Python 3.8+ is installed
- Try: python3 --version
- Download from: https://www.python.org

### Issue: pip command not found
- Try: python -m pip install -r requirements.txt

### Issue: Permission denied (macOS/Linux)
- Try: sudo python3 -m pip install -r requirements.txt

### Issue: ModuleNotFoundError
- Ensure virtual environment is activated
- Reinstall: pip install -r requirements.txt --force-reinstall

### Issue: Port 8501 already in use
- Use: streamlit run app.py --server.port 8502
- Or kill process using the port


## VERIFYING INSTALLATION

After installation, test each module:

```bash
# Test image analysis
python -c "from src.image_analysis import ImageAnalyzer; print('✓ ImageAnalyzer imported')"

# Test recommender
python -c "from src.outfit_recommender import OutfitRecommender; print('✓ OutfitRecommender imported')"

# Test rating
python -c "from src.rating_logic import LookRating; print('✓ LookRating imported')"

# Test Streamlit
streamlit --version
```

All should show success messages.


## RUNNING TESTS

To verify the system works without the UI:

```python
# Test script
from src.image_analysis import ImageAnalyzer
from src.outfit_recommender import OutfitRecommender
from src.rating_logic import LookRating

# Create instances
analyzer = ImageAnalyzer()
recommender = OutfitRecommender()
rater = LookRating()

print("✓ All modules loaded successfully!")
print("✓ System ready to use!")
```


## CONFIGURATION

### Change Recommendation Database
Edit: src/constants.py
Add new outfit types, colors, or styles in OUTFIT_RECOMMENDATIONS

### Customize UI Colors
Edit: app.py
Modify the CSS in st.markdown() for custom styling

### Adjust Analysis Sensitivity
Edit: src/image_analysis.py
Modify confidence thresholds and HSV ranges


## PERFORMANCE TIPS

1. Use high-quality images (clear, good lighting)
2. Ensure face is clearly visible
3. Keep app running - first load takes longer
4. Close other heavy applications
5. Use good internet connection (for initial MediaPipe download)

## DEVELOPMENT MODE

Run with debug mode:
```bash
streamlit run app.py --logger.level=debug
```

Run with auto-reloading:
```bash
streamlit run app.py --server.runOnSave=true
```

## DEPLOYMENT

To deploy to a server:
1. Install Python on server
2. Clone repository
3. Create virtual environment
4. Install dependencies
5. Run: streamlit run app.py --server.headless true

For production, consider using:
- Streamlit Cloud (free tier available)
- AWS/Google Cloud
- Docker containerization

## NEXT STEPS

1. Start the application: streamlit run app.py
2. Upload your first photo
3. Explore the three outfit styles
4. Get your personalized recommendations
5. Share results with friends!

---

For detailed information, see README.md
