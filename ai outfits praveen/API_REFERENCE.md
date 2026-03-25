"""
API DOCUMENTATION
AI Outfit Recommendation System - Complete API Reference
"""

# ============================================================================
# IMAGE ANALYSIS MODULE - api_reference.image_analysis
# ============================================================================

"""
CLASS: ImageAnalyzer

Purpose: Analyzes uploaded images for skin tone, face shape, and body structure

METHODS:

1. __init__()
   Initialize the ImageAnalyzer with MediaPipe face detection
   
   Returns: None
   Example:
       analyzer = ImageAnalyzer()

2. load_image(uploaded_file)
   Load image from an uploaded file
   
   Args:
       uploaded_file: Streamlit UploadedFile object
   
   Returns:
       np.ndarray: cv2 image in BGR format
       None: If image loading fails
   
   Example:
       img = analyzer.load_image(uploaded_file)

3. analyze_skin_tone(image)
   Analyze skin tone from the image using HSV color space
   
   Args:
       image: cv2 image in BGR format
   
   Returns:
       dict: {
           'tone': str ('light', 'medium', 'dark'),
           'confidence': float (0-1),
           'message': str (description),
           'hsv_values': dict (optional)
       }
   
   Example:
       result = analyzer.analyze_skin_tone(image)
       print(result['tone'])  # 'medium'

4. analyze_face_shape(image)
   Detect and classify face shape based on bounding box aspect ratio
   
   Args:
       image: cv2 image in BGR format
   
   Returns:
       dict: {
           'shape': str ('round', 'oval', 'square', 'heart', 'oblong'),
           'confidence': float (0-1),
           'message': str (description),
           'aspect_ratio': float
       }
   
   Example:
       result = analyzer.analyze_face_shape(image)
       print(result['shape'])  # 'oval'

5. analyze_body_structure(image)
   Estimate body structure from image composition
   
   Args:
       image: cv2 image in BGR format
   
   Returns:
       dict: {
           'structure': str ('slim', 'average', 'athletic'),
           'confidence': float (0-1),
           'message': str (description),
           'area_ratio': float
       }
   
   Example:
       result = analyzer.analyze_body_structure(image)
       print(result['structure'])  # 'average'

6. comprehensive_analysis(image)
   Perform all analysis types in one call
   
   Args:
       image: cv2 image in BGR format
   
   Returns:
       dict: {
           'skin_tone': dict (from analyze_skin_tone),
           'face_shape': dict (from analyze_face_shape),
           'body_structure': dict (from analyze_body_structure),
           'image_quality': dict (quality metrics)
       }
   
   Example:
       analysis = analyzer.comprehensive_analysis(image)
       print(analysis.keys())  # ['skin_tone', 'face_shape', 'body_structure', 'image_quality']

"""

# ============================================================================
# OUTFIT RECOMMENDATION MODULE - api_reference.outfit_recommender
# ============================================================================

"""
CLASS: OutfitRecommender

Purpose: Generates personalized outfit recommendations based on analysis results

METHODS:

1. __init__()
   Initialize the OutfitRecommender with recommendation database
   
   Returns: None
   Example:
       recommender = OutfitRecommender()

2. get_recommendations(analysis_results, outfit_type)
   Generate outfit recommendations
   
   Args:
       analysis_results: dict from ImageAnalyzer.comprehensive_analysis()
       outfit_type: str ('traditional', 'western', 'casual')
   
   Returns:
       dict: {
           'outfit_type': str,
           'skin_tone': str,
           'face_shape': str,
           'body_structure': str,
           'colors': dict {
               'primary': str,
               'secondary': str,
               'accent': str,
               'reasoning': str
           },
           'styles': dict {
               'primary': str,
               'secondary': str,
               'consideration': str,
               'fit_recommendation': str
           },
           'accessories': dict {
               'recommended': list,
               'styling_note': str,
               'avoid': str
           },
           'tips': list (of styling tips),
           'confidence': float (0-1)
       }
   
   Example:
       rec = recommender.get_recommendations(analysis, 'traditional')
       print(rec['colors']['primary'])  # 'Deep Gold'

3. _select_colors(color_options, face_shape)
   [INTERNAL] Select optimal colors based on face shape
   
   Args:
       color_options: list of colors
       face_shape: str (face shape type)
   
   Returns:
       dict with primary, secondary, accent colors and reasoning

4. _select_styles(style_options, body_structure, outfit_type)
   [INTERNAL] Select appropriate styles based on body structure
   
   Args:
       style_options: list of styles
       body_structure: str (body type)
       outfit_type: str (outfit type)
   
   Returns:
       dict with primary, secondary styles and consideration

5. _select_accessories(accessory_options, face_shape, body_structure, outfit_type)
   [INTERNAL] Select recommended accessories
   
   Args:
       accessory_options: list of accessories
       face_shape: str
       body_structure: str
       outfit_type: str
   
   Returns:
       dict with recommended accessories and styling notes

6. _generate_styling_tips(face_shape, body_structure, outfit_type)
   [INTERNAL] Generate personalized styling tips
   
   Args:
       face_shape: str
       body_structure: str
       outfit_type: str
   
   Returns:
       list of styling tips

"""

# ============================================================================
# RATING SYSTEM MODULE - api_reference.rating_logic
# ============================================================================

"""
CLASS: LookRating

Purpose: Rates the outfit look and generates compliments

METHODS:

1. __init__()
   Initialize the LookRating system
   
   Returns: None
   Example:
       rater = LookRating()

2. rate_look(analysis_results, recommendation, outfit_type)
   Generate a complete rating with analysis breakdown
   
   Args:
       analysis_results: dict from ImageAnalyzer.comprehensive_analysis()
       recommendation: dict from OutfitRecommender.get_recommendations()
       outfit_type: str ('traditional', 'western', 'casual')
   
   Returns:
       dict: {
           'numeric_rating': int (1-10),
           'star_rating': str (emoji stars),
           'description': str (rating description),
           'compliment': str (personalized compliment),
           'breakdown': dict (detailed breakdown of factors),
           'recommendations_to_improve': list (tips to improve look)
       }
   
   Example:
       rating = rater.rate_look(analysis, recommendation, 'traditional')
       print(rating['numeric_rating'])  # 8
       print(rating['compliment'])  # "Absolutely stunning!"

3. _calculate_rating(analysis_results, recommendation, outfit_type)
   [INTERNAL] Calculate numeric rating (1-10)
   
   Args:
       analysis_results: dict
       recommendation: dict
       outfit_type: str
   
   Returns:
       int: rating from 1-10

4. _get_star_rating(numeric_rating)
   [INTERNAL] Convert numeric rating to star representation
   
   Args:
       numeric_rating: int (1-10)
   
   Returns:
       str: emoji stars (e.g., "⭐⭐⭐⭐⭐")

5. _get_description(rating)
   [INTERNAL] Get description based on rating
   
   Args:
       rating: int (1-10)
   
   Returns:
       str: rating description

6. _get_compliment(rating)
   [INTERNAL] Get personalized compliment
   
   Args:
       rating: int (1-10)
   
   Returns:
       str: compliment text

7. _get_rating_breakdown(analysis_results, recommendation)
   [INTERNAL] Provide detailed breakdown of rating factors
   
   Args:
       analysis_results: dict
       recommendation: dict
   
   Returns:
       dict: breakdown of all factors influencing rating

8. _get_improvement_tips(rating, outfit_type)
   [INTERNAL] Get tips based on current rating
   
   Args:
       rating: int (1-10)
       outfit_type: str
   
   Returns:
       list: improvement suggestions

"""

# ============================================================================
# CONSTANTS MODULE - api_reference.constants
# ============================================================================

"""
IMPORTANT DICTIONARIES AND CONSTANTS:

1. OUTFIT_TYPES
   Available outfit type options
   
   Structure: {
       'traditional': 'Traditional',
       'western': 'Western',
       'casual': 'Casual'
   }

2. SKIN_TONES
   Available skin tone categories
   
   Structure: {
       'light': 'Light',
       'medium': 'Medium',
       'dark': 'Dark'
   }

3. FACE_SHAPES
   Available face shape options
   
   Structure: {
       'round': 'Round',
       'oval': 'Oval',
       'square': 'Square',
       'heart': 'Heart',
       'oblong': 'Oblong'
   }

4. OUTFIT_RECOMMENDATIONS
   Main recommendation database
   
   Structure: {
       'outfit_type': {
           'skin_tone': {
               'colors': [list of color names],
               'styles': [list of style names],
               'accessories': [list of accessory names]
           }
       }
   }
   
   Example access:
       colors = OUTFIT_RECOMMENDATIONS['traditional']['medium']['colors']
       # Returns: ['Warm Gold', 'Deep Red', 'Rich Green', 'Maroon']

5. RATING_DESCRIPTIONS
   Mapping of rating ranges to descriptions
   
   Structure: {
       (min, max): 'description'
   }
   
   Example:
       (8, 9): 'Excellent - Confident and impressive appearance'

6. COMPLIMENTS
   Mapping of rating ranges to compliment lists
   
   Structure: {
       (min, max): [list of compliments]
   }

"""

# ============================================================================
# WORKFLOW EXAMPLES
# ============================================================================

"""
EXAMPLE 1: Complete Analysis and Recommendation Flow

    from src.image_analysis import ImageAnalyzer
    from src.outfit_recommender import OutfitRecommender
    from src.rating_logic import LookRating
    import streamlit as st
    
    # Step 1: Load and analyze image
    uploaded_file = st.file_uploader('Upload image')
    if uploaded_file:
        analyzer = ImageAnalyzer()
        image = analyzer.load_image(uploaded_file)
        analysis = analyzer.comprehensive_analysis(image)
        
        # Step 2: Get recommendations
        recommender = OutfitRecommender()
        outfit_type = 'traditional'  # User choice
        recommendation = recommender.get_recommendations(analysis, outfit_type)
        
        # Step 3: Rate the look
        rater = LookRating()
        rating = rater.rate_look(analysis, recommendation, outfit_type)
        
        # Step 4: Display results
        st.write(f"Rating: {rating['numeric_rating']}/10")
        st.write(f"Compliment: {rating['compliment']}")

EXAMPLE 2: Access Skin Tone Analysis

    analysis = analyzer.comprehensive_analysis(image)
    skin_tone_result = analysis['skin_tone']
    
    print(f"Tone: {skin_tone_result['tone']}")          # 'light', 'medium', 'dark'
    print(f"Confidence: {skin_tone_result['confidence']}")  # 0.0-1.0

EXAMPLE 3: Access Recommendation Details

    recommendation = recommender.get_recommendations(analysis, 'western')
    
    colors = recommendation['colors']
    print(f"Primary color: {colors['primary']}")
    print(f"Why this color: {colors['reasoning']}")
    
    styles = recommendation['styles']
    print(f"Recommended style: {styles['primary']}")
    print(f"For your {recommendation['body_structure']} build")

EXAMPLE 4: Access Rating Breakdown

    rating = rater.rate_look(analysis, recommendation, 'casual')
    
    breakdown = rating['breakdown']
    for category, details in breakdown.items():
        print(f"{category}: {details}")
    
    improvement_tips = rating['recommendations_to_improve']
    for i, tip in enumerate(improvement_tips, 1):
        print(f"{i}. {tip}")

"""

# ============================================================================
# DATA STRUCTURES
# ============================================================================

"""
ANALYSIS_RESULTS Structure:
{
    'skin_tone': {
        'tone': 'light' | 'medium' | 'dark',
        'confidence': float (0-1),
        'message': str,
        'hsv_values': {'h': float, 's': float, 'v': float}
    },
    'face_shape': {
        'shape': 'round' | 'oval' | 'square' | 'heart' | 'oblong',
        'confidence': float (0-1),
        'message': str,
        'aspect_ratio': float
    },
    'body_structure': {
        'structure': 'slim' | 'average' | 'athletic',
        'confidence': float (0-1),
        'message': str,
        'area_ratio': float
    },
    'image_quality': {
        'quality': 'good' | 'blurry' | 'poor lighting',
        'score': float (0-1),
        'laplacian_variance': float,
        'brightness': float
    }
}

RECOMMENDATION Structure:
{
    'outfit_type': str,
    'skin_tone': str,
    'face_shape': str,
    'body_structure': str,
    'colors': {
        'primary': str,
        'secondary': str,
        'accent': str,
        'reasoning': str
    },
    'styles': {
        'primary': str,
        'secondary': str,
        'consideration': str,
        'fit_recommendation': str
    },
    'accessories': {
        'recommended': [str, ...],
        'styling_note': str,
        'avoid': str
    },
    'tips': [str, ...],
    'confidence': float (0-1)
}

RATING_RESULT Structure:
{
    'numeric_rating': int (1-10),
    'star_rating': str,
    'description': str,
    'compliment': str,
    'breakdown': {
        'image_quality': {...},
        'skin_tone_analysis': {...},
        'face_shape_analysis': {...},
        'body_structure_analysis': {...},
        'outfit_match': {...}
    },
    'recommendations_to_improve': [str, ...]
}

"""

# ============================================================================
# ERROR HANDLING
# ============================================================================

"""
COMMON ERRORS AND SOLUTIONS:

1. "Face not detected"
   - Ensure face is clearly visible in image
   - Check image brightness and contrast
   - Try image with better lighting

2. "Could not decode image"
   - Verify image format is JPG or PNG
   - Check file is not corrupted
   - Ensure file size is under 5MB

3. "Invalid outfit type"
   - Use only: 'traditional', 'western', 'casual'
   - Ensure lowercase spelling

4. MediaPipe errors
   - Update: pip install --upgrade mediapipe
   - Verify NumPy version compatibility
   - Check disk space for model files

5. Streamlit "Port already in use"
   - Run: streamlit run app.py --server.port 8502
   - Or kill process using port 8501

"""

# ============================================================================
# PERFORMANCE TIPS
# ============================================================================

"""
OPTIMIZATION RECOMMENDATIONS:

1. Image Quality
   - Use high-resolution images (minimum 480p)
   - Ensure good lighting
   - Face should occupy at least 20% of image

2. Processing Speed
   - First load is slower (MediaPipe initialization)
   - Subsequent analyses are faster
   - Close unnecessary applications

3. Accuracy
   - Better image quality = higher confidence
   - Clear face visibility improves detection
   - Multiple angles can increase reliability

4. Memory Usage
   - Images are not stored permanently by default
   - Configure in config.py if needed
   - Clear cache periodically for long sessions

"""

# ============================================================================
# EXTENDING THE SYSTEM
# ============================================================================

"""
HOW TO ADD NEW FEATURES:

1. Add New Outfit Type:
   - Edit: src/constants.py
   - Add to OUTFIT_TYPES
   - Add recommendations for all skin tones in OUTFIT_RECOMMENDATIONS

2. Add New Recommendation:
   - Edit: src/outfit_recommender.py
   - Modify recommendation rules in OutfitRecommender class

3. Add New Analysis Feature:
   - Edit: src/image_analysis.py
   - Add new method to ImageAnalyzer class
   - Call it from comprehensive_analysis()

4. Add New UI Component:
   - Edit: app.py
   - Modify Streamlit layout and styling

"""
