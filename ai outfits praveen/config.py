"""
Configuration file for AI Outfit Recommendation System
Centralized settings and environment variables
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================

APP_NAME = "AI Outfit Recommendation System"
APP_VERSION = "1.0.0"
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# ============================================================================
# FILE UPLOAD SETTINGS
# ============================================================================

MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")

# ============================================================================
# IMAGE ANALYSIS SETTINGS
# ============================================================================

# Face detection confidence threshold
FACE_DETECTION_CONFIDENCE = 0.5

# Image quality thresholds
MIN_LAPLACIAN_VARIANCE = 100  # For blur detection
MIN_BRIGHTNESS = 50
MAX_BRIGHTNESS = 200

# ============================================================================
# RECOMMENDATION SETTINGS
# ============================================================================

# Number of recommendations per category
NUM_COLOR_SUGGESTIONS = 3
NUM_STYLE_SUGGESTIONS = 2
NUM_ACCESSORY_SUGGESTIONS = 2

# Confidence thresholds
MIN_ANALYSIS_CONFIDENCE = 0.5
MIN_RECOMMENDATION_CONFIDENCE = 0.6

# ============================================================================
# RATING SETTINGS
# ============================================================================

MIN_RATING = 1
MAX_RATING = 10
RATING_SCALE = "1-10"

# ============================================================================
# UI/UX SETTINGS
# ============================================================================

# Streamlit page configuration
PAGE_LAYOUT = "wide"
PAGE_INITIAL_SIDEBAR = "collapsed"

# Color scheme
PRIMARY_COLOR = "#667eea"
SECONDARY_COLOR = "#764ba2"
ACCENT_COLOR = "#f093fb"
BACKGROUND_COLOR = "#f5f7fa"

# ============================================================================
# DISPLAY SETTINGS
# ============================================================================

# Emoji usage
USE_EMOJI = True
SHOW_CONFIDENCE_SCORES = True
SHOW_ANALYSIS_BREAKDOWN = True

# ============================================================================
# ANALYSIS FEATURE SETTINGS
# ============================================================================

# Skin tone detection
SKIN_TONE_CATEGORIES = ['light', 'medium', 'dark']
SKIN_TONE_HSV_THRESHOLDS = {
    'light': (180, float('inf')),
    'medium': (130, 180),
    'dark': (0, 130)
}

# Face shape detection
FACE_SHAPES = ['round', 'oval', 'square', 'heart', 'oblong']
FACE_SHAPE_ASPECT_RATIOS = {
    'oblong': (1.0, float('inf')),
    'oval': (0.85, 1.0),
    'square': (0.75, 0.85),
    'round': (0.0, 0.75)
}

# Body structure detection
BODY_STRUCTURES = ['slim', 'average', 'athletic']
BODY_STRUCTURE_AREA_RATIOS = {
    'slim': (0.15, float('inf')),
    'average': (0.08, 0.15),
    'athletic': (0.0, 0.08)
}

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "app.log")
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() == "true"

# ============================================================================
# API SETTINGS (for future use)
# ============================================================================

API_ENABLED = False
API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = int(os.getenv("API_PORT", "5000"))

# ============================================================================
# DATABASE SETTINGS (for future use)
# ============================================================================

DATABASE_ENABLED = False
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================

# Cache settings
ENABLE_CACHING = True
CACHE_TTL = 3600  # seconds

# Image processing
RESIZE_LARGE_IMAGES = True
MAX_IMAGE_WIDTH = 1280
MAX_IMAGE_HEIGHT = 720

# ============================================================================
# SECURITY SETTINGS
# ============================================================================

# Data retention
DELETE_IMAGES_AFTER_ANALYSIS = True
IMAGE_RETENTION_TIME = 300  # seconds

# Session security
SESSION_TIMEOUT = 1800  # seconds (30 minutes)
SECURE_SESSION = True

# ============================================================================
# FEATURE FLAGS
# ============================================================================

ENABLE_IMAGE_ANALYSIS = True
ENABLE_RECOMMENDATIONS = True
ENABLE_RATING_SYSTEM = True
ENABLE_STYLING_TIPS = True
ENABLE_BREAKDOWN_DETAILS = True

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_config(key, default=None):
    """
    Get configuration value by key
    
    Args:
        key: Configuration key
        default: Default value if key not found
        
    Returns:
        Configuration value
    """
    return globals().get(key, default)

def is_feature_enabled(feature_name):
    """
    Check if a feature is enabled
    
    Args:
        feature_name: Name of the feature
        
    Returns:
        Boolean indicating if feature is enabled
    """
    feature_key = f"ENABLE_{feature_name.upper()}"
    return globals().get(feature_key, False)

# ============================================================================
# PRINT CONFIG (for debugging)
# ============================================================================

if DEBUG_MODE:
    print("=" * 60)
    print("AI OUTFIT RECOMMENDATION SYSTEM - CONFIGURATION")
    print("=" * 60)
    print(f"App Name: {APP_NAME} v{APP_VERSION}")
    print(f"Debug Mode: {DEBUG_MODE}")
    print(f"Max File Size: {MAX_FILE_SIZE_MB}MB")
    print(f"Face Detection Confidence: {FACE_DETECTION_CONFIDENCE}")
    print("=" * 60)
