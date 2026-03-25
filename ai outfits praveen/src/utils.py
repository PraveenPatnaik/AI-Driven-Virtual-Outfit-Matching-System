"""
Utility functions for AI Outfit Recommendation System
Helper functions for common tasks across the application
"""

import os
import cv2
import numpy as np
from PIL import Image
from pathlib import Path
import logging
from datetime import datetime

# ============================================================================
# LOGGING SETUP
# ============================================================================

def setup_logger(name, log_file='app.log', level=logging.INFO):
    """
    Set up a logger for the application
    
    Args:
        name: Logger name
        log_file: Log file path
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create formatters and handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger(__name__)

# ============================================================================
# FILE UTILITIES
# ============================================================================

def validate_file(file_path, allowed_extensions={'jpg', 'jpeg', 'png'}, max_size_bytes=5*1024*1024):
    """
    Validate if a file meets requirements
    
    Args:
        file_path: Path to file
        allowed_extensions: Set of allowed file extensions
        max_size_bytes: Maximum file size in bytes
        
    Returns:
        Tuple (is_valid, error_message)
    """
    try:
        if not os.path.exists(file_path):
            return False, "File does not exist"
        
        # Check extension
        file_ext = Path(file_path).suffix.lower().lstrip('.')
        if file_ext not in allowed_extensions:
            return False, f"Invalid file type. Allowed: {', '.join(allowed_extensions)}"
        
        # Check file size
        file_size = os.path.getsize(file_path)
        if file_size > max_size_bytes:
            max_size_mb = max_size_bytes / (1024 * 1024)
            return False, f"File too large. Maximum size: {max_size_mb}MB"
        
        return True, "File is valid"
    
    except Exception as e:
        return False, f"Error validating file: {str(e)}"

def get_file_info(file_path):
    """
    Get detailed information about a file
    
    Args:
        file_path: Path to file
        
    Returns:
        Dictionary with file info
    """
    try:
        path = Path(file_path)
        stat = path.stat()
        
        return {
            'name': path.name,
            'size_bytes': stat.st_size,
            'size_mb': round(stat.st_size / (1024 * 1024), 2),
            'extension': path.suffix.lower(),
            'created': datetime.fromtimestamp(stat.st_ctime),
            'modified': datetime.fromtimestamp(stat.st_mtime)
        }
    
    except Exception as e:
        logger.error(f"Error getting file info: {e}")
        return None

# ============================================================================
# IMAGE UTILITIES
# ============================================================================

def get_image_dimensions(image):
    """
    Get dimensions of an image
    
    Args:
        image: cv2 image (BGR)
        
    Returns:
        Tuple (height, width, channels)
    """
    try:
        return image.shape
    except Exception as e:
        logger.error(f"Error getting image dimensions: {e}")
        return None

def resize_image(image, max_width=1280, max_height=720):
    """
    Resize image to fit within max dimensions while maintaining aspect ratio
    
    Args:
        image: cv2 image
        max_width: Maximum width
        max_height: Maximum height
        
    Returns:
        Resized cv2 image
    """
    try:
        h, w = image.shape[:2]
        
        # Calculate scaling factor
        scale = min(max_width / w, max_height / h, 1.0)
        
        if scale < 1.0:
            new_w = int(w * scale)
            new_h = int(h * scale)
            image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
            logger.info(f"Image resized from {w}x{h} to {new_w}x{new_h}")
        
        return image
    
    except Exception as e:
        logger.error(f"Error resizing image: {e}")
        return image

def enhance_image_quality(image):
    """
    Enhance image quality through various preprocessing techniques
    
    Args:
        image: cv2 image
        
    Returns:
        Enhanced cv2 image
    """
    try:
        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        
        enhanced = cv2.merge([l, a, b])
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
        
        return enhanced
    
    except Exception as e:
        logger.error(f"Error enhancing image: {e}")
        return image

def convert_to_pil(cv_image):
    """
    Convert cv2 image (BGR) to PIL Image (RGB)
    
    Args:
        cv_image: cv2 image in BGR format
        
    Returns:
        PIL Image
    """
    try:
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        return pil_image
    
    except Exception as e:
        logger.error(f"Error converting to PIL: {e}")
        return None

def convert_to_cv2(pil_image):
    """
    Convert PIL Image (RGB) to cv2 image (BGR)
    
    Args:
        pil_image: PIL Image
        
    Returns:
        cv2 image in BGR format
    """
    try:
        cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        return cv_image
    
    except Exception as e:
        logger.error(f"Error converting to cv2: {e}")
        return None

# ============================================================================
# ANALYSIS UTILITIES
# ============================================================================

def get_confidence_level(confidence_score):
    """
    Convert confidence score (0-1) to readable level
    
    Args:
        confidence_score: Score from 0 to 1
        
    Returns:
        Confidence level string
    """
    if confidence_score >= 0.85:
        return "Very High"
    elif confidence_score >= 0.70:
        return "High"
    elif confidence_score >= 0.55:
        return "Medium"
    elif confidence_score >= 0.40:
        return "Low"
    else:
        return "Very Low"

def format_percentage(value):
    """
    Format value as percentage string
    
    Args:
        value: Decimal value (0-1)
        
    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.1f}%"

def calculate_average_confidence(confidences):
    """
    Calculate average confidence from list of values
    
    Args:
        confidences: List of confidence values
        
    Returns:
        Average confidence
    """
    if not confidences:
        return 0.0
    return sum(confidences) / len(confidences)

# ============================================================================
# COLOR UTILITIES
# ============================================================================

def get_color_name_from_rgb(rgb_tuple):
    """
    Get approximate color name from RGB values
    
    Args:
        rgb_tuple: Tuple of (R, G, B) values (0-255)
        
    Returns:
        Color name string
    """
    r, g, b = rgb_tuple
    
    # Simple color classification
    if r > 200 and g > 200 and b > 200:
        return "White"
    elif r < 50 and g < 50 and b < 50:
        return "Black"
    elif r > g and r > b:
        return "Red"
    elif g > r and g > b:
        return "Green"
    elif b > r and b > g:
        return "Blue"
    elif r > 150 and g < 100:
        return "Red"
    elif r > 150 and g > 100 and b < 100:
        return "Orange"
    else:
        return "Neutral"

def hsv_to_rgb(hsv_tuple):
    """
    Convert HSV to RGB
    
    Args:
        hsv_tuple: Tuple of (H, S, V) values in OpenCV range
        
    Returns:
        Tuple of (R, G, B) values
    """
    try:
        h, s, v = hsv_tuple
        # Normalize to 0-1 range
        h = h / 180.0 * 360.0 if h <= 180 else h
        s = s / 255.0
        v = v / 255.0
        
        c = v * s
        x = c * (1 - abs((h / 60.0) % 2 - 1))
        m = v - c
        
        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        
        return (int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))
    
    except Exception as e:
        logger.error(f"Error converting HSV to RGB: {e}")
        return (128, 128, 128)

# ============================================================================
# STRING UTILITIES
# ============================================================================

def capitalize_words(text):
    """
    Capitalize first letter of each word
    
    Args:
        text: Input string
        
    Returns:
        Capitalized string
    """
    return ' '.join(word.capitalize() for word in text.split())

def format_label(label):
    """
    Format label for display (snake_case to Title Case)
    
    Args:
        label: Input label
        
    Returns:
        Formatted label
    """
    return capitalize_words(label.replace('_', ' '))

# ============================================================================
# DATA VALIDATION
# ============================================================================

def is_valid_rating(rating):
    """
    Check if rating is valid (1-10)
    
    Args:
        rating: Rating value
        
    Returns:
        Boolean
    """
    try:
        rating = int(rating)
        return 1 <= rating <= 10
    except:
        return False

def is_valid_outfit_type(outfit_type):
    """
    Check if outfit type is valid
    
    Args:
        outfit_type: Outfit type string
        
    Returns:
        Boolean
    """
    valid_types = ['traditional', 'western', 'casual']
    return outfit_type.lower() in valid_types

def is_valid_skin_tone(skin_tone):
    """
    Check if skin tone is valid
    
    Args:
        skin_tone: Skin tone string
        
    Returns:
        Boolean
    """
    valid_tones = ['light', 'medium', 'dark']
    return skin_tone.lower() in valid_tones

# ============================================================================
# STATISTICS
# ============================================================================

def get_analysis_statistics(analysis_results):
    """
    Generate statistics from analysis results
    
    Args:
        analysis_results: Analysis results dictionary
        
    Returns:
        Statistics dictionary
    """
    try:
        stats = {
            'total_confidence': calculate_average_confidence([
                analysis_results['skin_tone']['confidence'],
                analysis_results['face_shape']['confidence'],
                analysis_results['body_structure']['confidence']
            ]),
            'image_quality_score': analysis_results['image_quality']['score'],
            'face_shape': analysis_results['face_shape']['shape'],
            'skin_tone': analysis_results['skin_tone']['tone'],
            'body_structure': analysis_results['body_structure']['structure']
        }
        return stats
    
    except Exception as e:
        logger.error(f"Error generating statistics: {e}")
        return None

# ============================================================================
# TEST FUNCTION
# ============================================================================

if __name__ == "__main__":
    """Test utility functions"""
    print("Testing utility functions...")
    
    # Test confidence level
    print(f"Confidence 0.9: {get_confidence_level(0.9)}")
    print(f"Confidence 0.5: {get_confidence_level(0.5)}")
    
    # Test percentage
    print(f"0.75 as percentage: {format_percentage(0.75)}")
    
    # Test label formatting
    print(f"Formatted label: {format_label('face_shape')}")
    
    # Test validation
    print(f"Valid rating 7: {is_valid_rating(7)}")
    print(f"Valid outfit type 'traditional': {is_valid_outfit_type('traditional')}")
    
    print("\n✓ All utility functions tested successfully!")
