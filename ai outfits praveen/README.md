# 👗 AI Outfit Recommendation System

A complete Python-based application that analyzes user photos and provides personalized outfit recommendations using advanced image analysis and AI logic.

## 🎯 Project Overview

This system helps users discover perfect outfits by:
1. **Analyzing** user photos for skin tone, face shape, and body structure
2. **Processing** outfit preferences (Traditional, Western, or Casual)
3. **Recommending** suitable color palettes, styles, and accessories
4. **Rating** the final outfit look with personalized compliments

## ✨ Features

### Core Features
- 📸 **Image Upload**: Support for JPG/PNG images up to 5MB
- 🎨 **Image Analysis**: AI-powered detection of skin tone, face shape, and body structure
- 👔 **Outfit Recommendation**: Personalized suggestions based on analyzed features
- ⭐ **Look Rating**: Numeric (1-10) and star ratings with compliments
- 💡 **Styling Tips**: Detailed guidance for enhancing your look

### Technology Features
- 🔍 **Computer Vision**: OpenCV & MediaPipe for accurate face and feature detection
- 🤖 **AI Logic**: Rule-based recommendation engine
- 🌐 **Web Interface**: Streamlit for seamless user experience
- 🎯 **Privacy First**: No permanent image storage

## 📁 Project Structure

```
ai outfits/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── src/
│   ├── image_analysis.py    # Computer vision module (ImageAnalyzer class)
│   ├── outfit_recommender.py # Recommendation engine (OutfitRecommender class)
│   ├── rating_logic.py      # Rating system (LookRating class)
│   └── constants.py         # Configuration and outfit database
└── assets/                  # Assets folder (for future use)
```

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Main programming language
- **Streamlit**: Web framework for UI (Python-native)

### Computer Vision & AI
- **OpenCV**: Image processing and analysis
- **MediaPipe**: Face detection and landmark detection
- **NumPy**: Numerical computations

### Additional
- **Pillow**: Image handling in web interface
- **Python-dotenv**: Environment configuration

## 📋 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone/Download the Project
```bash
cd "c:\Users\msi\ai outfits"
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 🎮 How to Use

### Step 1: Upload Photo
1. Click the file uploader
2. Select a clear photo of yourself (JPG/PNG)
3. Ensure your face and upper body are visible

### Step 2: Choose Outfit Style
Select one of three options:
- **👗 Traditional**: Elegant ethnic and formal wear
- **🤠 Western**: Modern casual to formal western clothing
- **👕 Casual**: Comfortable everyday wear

### Step 3: View Results
The system provides:
- **Analysis Tab**: Detected features (skin tone, face shape, body structure)
- **Recommendations Tab**: Color palettes, outfit styles, and accessories
- **Rating Tab**: Overall look rating with compliments and tips

## 🔬 Technical Details

### Image Analysis Module (`image_analysis.py`)

**ImageAnalyzer Class**:
- `load_image()`: Load and decode uploaded images
- `analyze_skin_tone()`: Detect skin tone using HSV color space
- `analyze_face_shape()`: Determine face shape from bounding box
- `analyze_body_structure()`: Estimate body type from image composition
- `comprehensive_analysis()`: Run all analyses at once

**Features Detected**:
- **Skin Tone**: Light, Medium, Dark (based on HSV value channel)
- **Face Shape**: Round, Oval, Square, Heart, Oblong (based on aspect ratio)
- **Body Structure**: Slim, Average, Athletic (based on face-to-image ratio)

### Outfit Recommendation Module (`outfit_recommender.py`)

**OutfitRecommender Class**:
- `get_recommendations()`: Generate outfit suggestions
- `_select_colors()`: Pick colors based on face shape
- `_select_styles()`: Choose styles based on body structure
- `_select_accessories()`: Recommend accessories
- `_generate_styling_tips()`: Create personalized tips

**Logic**:
- Rule-based system using feature-to-outfit mapping
- Database of 3 outfit types × 3 skin tones = 9 recommendation profiles
- Dynamic scoring based on analysis confidence

### Rating System (`rating_logic.py`)

**LookRating Class**:
- `rate_look()`: Calculate overall rating (1-10)
- `_calculate_rating()`: Weighted scoring from multiple factors
- `_get_star_rating()`: Convert numeric to visual rating
- `_get_compliment()`: Generate personalized compliments

**Rating Factors**:
- Image quality (weight: 40%)
- Feature detection confidence (weight: 40%)
- Body-outfit type match (weight: 20%)

## 📊 Recommendation Database

Outfit recommendations are stored in `constants.py` with structure:
```python
OUTFIT_RECOMMENDATIONS = {
    'outfit_type': {
        'skin_tone': {
            'colors': [...],
            'styles': [...],
            'accessories': [...]
        }
    }
}
```

**Outfit Types**: Traditional, Western, Casual
**Skin Tones**: Light, Medium, Dark
**Each has**: Colors, Styles, Accessories recommendations

## 🔒 Privacy & Security

- ✅ **No Storage**: Images are not permanently stored
- ✅ **Local Processing**: All analysis happens on your machine
- ✅ **No Cloud**: No data is sent to external servers
- ✅ **No Tracking**: User activity is not tracked

## 🐛 Troubleshooting

### Issue: "Face not detected"
- Ensure your face is clearly visible in the photo
- Try with better lighting
- Make sure the image is not blurry

### Issue: "Could not decode image"
- Verify the file is a valid JPG or PNG
- Check file size is under 5MB
- Try re-saving the image

### Issue: Streamlit not opening
- Ensure Streamlit is installed: `pip install streamlit`
- Try: `streamlit run app.py --logger.level=debug`
- Check firewall settings

### Issue: MediaPipe errors
- Update MediaPipe: `pip install --upgrade mediapipe`
- Ensure NumPy is compatible: `pip install numpy==1.24.3`

## 📈 Future Enhancements

Potential improvements for future versions:
- 🤖 ML-based outfit recommendations using trained models
- 🎭 Multiple face detection for group photos
- 👠 Shoe and bag recommendation system
- 🌈 Advanced color harmony analysis
- 📊 User preference learning
- 📱 Mobile app version
- ☁️ Cloud storage for saved recommendations
- 🎨 Virtual try-on feature

## 📝 Code Examples

### Using the ImageAnalyzer
```python
from src.image_analysis import ImageAnalyzer

analyzer = ImageAnalyzer()
img = analyzer.load_image(uploaded_file)
analysis = analyzer.comprehensive_analysis(img)

print(f"Skin Tone: {analysis['skin_tone']['tone']}")
print(f"Face Shape: {analysis['face_shape']['shape']}")
```

### Using the Recommender
```python
from src.outfit_recommender import OutfitRecommender

recommender = OutfitRecommender()
recommendation = recommender.get_recommendations(analysis, 'traditional')

print(f"Primary Color: {recommendation['colors']['primary']}")
print(f"Style: {recommendation['styles']['primary']}")
```

### Using the Rating System
```python
from src.rating_logic import LookRating

rater = LookRating()
rating = rater.rate_look(analysis, recommendation, 'traditional')

print(f"Rating: {rating['numeric_rating']}/10")
print(f"Compliment: {rating['compliment']}")
```

## 🤝 Contributing

To extend this project:
1. Add new outfit types in `constants.py`
2. Enhance image analysis in `image_analysis.py`
3. Add more recommendation rules in `outfit_recommender.py`
4. Improve UI components in `app.py`

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a comprehensive Python-based AI outfit recommendation system.
Python is the main language for all backend, AI, and CV logic.

## 📧 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review code comments in relevant modules
3. Ensure all dependencies are correctly installed

---

**Enjoy discovering your perfect outfit! 👗✨**
