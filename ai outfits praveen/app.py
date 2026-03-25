"""
AI Outfit Recommendation System - Main Application
A complete Python-based application for outfit recommendations using image analysis
Built with Streamlit for minimal, clean UI
"""


import streamlit as st
import io
import sys
import os
import cv2
import numpy as np
import time
from PIL import Image, ImageDraw, ImageFont

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from image_analysis import ImageAnalyzer
from outfit_recommender import OutfitRecommender
from amazon_suggestions import AmazonSuggestions
from outfit_visualizer import OutfitVisualizer
from constants import OUTFIT_TYPES

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="AI Outfit Recommendation",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

st.markdown("""
    <style>
    /* Main styling */
    * {
        margin: 0;
        padding: 0;
    }
    
    /* Background and general page */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Recommendation card */
    .recommendation-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 6px 15px rgba(102, 126, 234, 0.15);
        margin: 20px 0;
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .recommendation-card:hover {
        box-shadow: 0 12px 25px rgba(102, 126, 234, 0.25);
        transform: translateX(5px);
    }
    
    /* Analysis card */
    .analysis-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Rating card */
    .rating-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 15px;
        padding: 35px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.2);
        font-size: 1.1em;
    }
    
    /* Product card styling */
    .product-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 22px;
        margin: 15px 0;
        transition: all 0.3s ease;
        border: 2px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 6px 15px rgba(102, 126, 234, 0.2);
    }
    
    .product-card:hover {
        transform: scale(1.03);
        box-shadow: 0 12px 28px rgba(102, 126, 234, 0.4);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 12px;
        padding: 12px 28px !important;
        font-weight: bold;
        border: none;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        transition: all 0.3s ease;
        font-size: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.5);
    }
    
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* Title styling */
    h1 {
        color: #333;
        text-align: center;
        margin-bottom: 10px;
        font-size: 2.8em;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    h2 {
        color: #667eea;
        margin-top: 30px;
        margin-bottom: 20px;
        border-bottom: 3px solid #667eea;
        padding-bottom: 12px;
        font-size: 1.6em;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    h3 {
        color: #764ba2;
        margin-top: 18px;
        font-size: 1.3em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Metric styling */
    .metric-label {
        color: #666;
        font-size: 0.9em;
        font-weight: bold;
    }
    
    .metric-value {
        color: #333;
        font-size: 1.3em;
        font-weight: bold;
    }
    
    /* Success/info messages */
    .stSuccess {
        background-color: #d4edda !important;
    }
    
    .stInfo {
        background-color: #d1ecf1 !important;
    }
    
    /* File uploader */
    .stFileUploader {
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f0f2f6;
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    
    /* Interactive elements */
    .interactive-card {
        background: linear-gradient(135deg, #ffffff 0%, #f5f7ff 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 18px 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.12);
        transition: all 0.3s ease;
        border: 2px solid rgba(102, 126, 234, 0.1);
    }
    
    .interactive-card:hover {
        box-shadow: 0 12px 28px rgba(102, 126, 234, 0.2);
        transform: translateY(-4px);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    /* Section divider */
    .section-divider {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 4px;
        border-radius: 2px;
        margin: 20px 0;
    }
    
    /* Tab styling - Enhanced and Wider */
    .stTabs {
        margin: 30px 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(255, 255, 255, 0.9);
        padding: 15px 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        border-radius: 12px;
        padding: 14px 24px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        background: rgba(102, 126, 234, 0.1) !important;
        color: #333 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stTabs [data-baseweb="tab-list"] button:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%) !important;
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.3);
        border-color: #667eea;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4) !important;
        border-color: #667eea !important;
        transform: scale(1.02);
    }
    
    /* Tab content styling */
    .stTabs [data-baseweb="tab"] {
        padding: 30px 25px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def format_analysis_results(analysis):
    """Format analysis results for display"""
    return {
        'Gender': f"{analysis['gender']['gender']} (Confidence: {analysis['gender']['confidence']*100:.0f}%)",
        'Skin Tone': f"{analysis['skin_tone']['tone'].upper()} (Confidence: {analysis['skin_tone']['confidence']*100:.0f}%)",
        'Face Shape': f"{analysis['face_shape']['shape'].capitalize()} (Confidence: {analysis['face_shape']['confidence']*100:.0f}%)",
        'Body Structure': f"{analysis['body_structure']['structure'].capitalize()} (Confidence: {analysis['body_structure']['confidence']*100:.0f}%)",
        'Image Quality': f"{analysis['image_quality']['quality'].upper()} (Score: {analysis['image_quality']['score']*100:.0f}%)"
    }

# Rating UI removed — app focuses on analysis, recommendations, Amazon picks, and preview

def display_outfit_recommendation(recommendation):
    """Display outfit recommendation details"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 Color Palette")
        st.markdown(f"""
        - **Primary**: {recommendation['colors']['primary']}
        - **Secondary**: {recommendation['colors']['secondary']}
        - **Accent**: {recommendation['colors']['accent']}
        
        *{recommendation['colors']['reasoning']}*
        """)
        
        st.subheader("👚 Outfit Styles")
        st.markdown(f"""
        - **Primary Style**: {recommendation['styles']['primary']}
        - **Secondary Style**: {recommendation['styles']['secondary']}
        
        *{recommendation['styles']['consideration']}*
        """)
    
    with col2:
        st.subheader("✨ Accessories")
        st.markdown(f"""
        **Recommended Accessories:**
        """)
        for acc in recommendation['accessories']['recommended']:
            st.markdown(f"- {acc}")
        
        st.markdown(f"""
        *{recommendation['accessories']['styling_note']}*
        """)
    
    st.subheader("💡 Styling Tips")
    for i, tip in enumerate(recommendation['tips'], 1):
        st.markdown(f"{i}. {tip}")

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application flow"""
    
    # Header with enhanced styling
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='font-size: 3.2em; margin: 0; color: #333;'>✨ 👗 AI Outfit Recommendation System 👗 ✨</h1>
        <p style='font-size: 1.2em; color: #667eea; font-weight: 600; margin-top: 10px;'>
            💫 Discover the Perfect Outfit Based on Your Unique Features & Style 💫
        </p>
        <p style='color: #999; font-size: 0.95em; margin-top: 10px;'>Powered by Advanced AI Analysis | Personalized Suggestions | Real-Time Visualization</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Decorative divider
    st.markdown("<div style='height: 3px; background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #667eea 100%); border-radius: 2px; margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # Initialize session state
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    if 'recommendation' not in st.session_state:
        st.session_state.recommendation = None
    
    
    # ========================================================================
    # STEP 1: IMAGE UPLOAD
    # ========================================================================
    
    with st.container():
        col_upload, col_info = st.columns([2, 1])
        
        with col_upload:
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.08) 0%, rgba(118, 75, 162, 0.08) 100%); 
                        border-radius: 12px; padding: 20px; border: 2px dashed #667eea;'>
                <h3 style='margin: 0 0 10px 0; color: #667eea;'>📸 UPLOAD YOUR PHOTO</h3>
                <p style='margin: 0 0 15px 0; color: #666; font-size: 0.95em;'>Show us your style! Upload a clear photo of yourself and let our AI work its magic ✨</p>
            </div>
            """, unsafe_allow_html=True)
            
            uploaded_file = st.file_uploader(
                label_visibility="collapsed",
                label="Choose an image (JPG or PNG)",
                type=['jpg', 'jpeg', 'png'],
                help="Upload a clear photo of yourself for outfit recommendations"
            )
        
        with col_info:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);'>
                <strong style='font-size: 1.15em; display: block; margin-bottom: 12px;'>✅ QUICK TIPS</strong>
                <div style='font-size: 0.9em; line-height: 1.8;'>
                    📷 <strong>Clear Photo</strong><br>
                    💡 <strong>Good Light</strong><br>
                    👤 <strong>Face Visible</strong><br>
                    📏 <strong>Upper Body</strong><br>
                    ⚡ <strong>Max 5 MB</strong>
                </div>
                <div style='margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.3); font-size: 0.85em; opacity: 0.9;'>
                    💬 Pro Tip: Stand in natural light for best results!
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    if uploaded_file is not None:
        # Read file bytes once to avoid file pointer issues
        file_bytes = uploaded_file.read()
        uploaded_file.seek(0)  # Reset file pointer for other operations
        # Store uploaded image bytes in session state for later use (preview tab)
        st.session_state['uploaded_file'] = file_bytes
        
        # Display uploaded image - smaller preview
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(240, 147, 251, 0.1) 0%, rgba(245, 87, 108, 0.1) 100%); 
                    border-radius: 15px; padding: 20px; margin: 20px 0;'>
            <h2 style='margin-top: 0; color: #764ba2;'>📷 Your Photo Preview</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col_img, col_space, col_note = st.columns([1, 0.5, 1.5])
        
        with col_img:
            image = Image.open(io.BytesIO(file_bytes))
            # Resize image for smaller preview
            max_width = 300
            ratio = max_width / image.width
            new_height = int(image.height * ratio)
            image_small = image.resize((max_width, new_height))
            st.image(image_small, use_column_width=True)
        
        with col_note:
            st.markdown("""
            <div style='background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); 
                        color: #155724; border-radius: 12px; padding: 15px; border-left: 4px solid #28a745;'>
                <strong>✅ Image Uploaded Successfully!</strong><br>
                📊 The system will now analyze your features and suggest perfect outfits!
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 2px; background: linear-gradient(90deg, #667eea 0%, transparent 100%); margin: 25px 0;'></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        outfit_type = None
        
        with col1:
            if st.button("👗 Traditional", use_container_width=True, key="trad_btn"):
                outfit_type = 'traditional'
                st.session_state.selected_style = 'traditional'
        
        with col2:
            if st.button("🤠 Western", use_container_width=True, key="west_btn"):
                outfit_type = 'western'
                st.session_state.selected_style = 'western'
        
        with col3:
            if st.button("👕 Casual", use_container_width=True, key="cas_btn"):
                outfit_type = 'casual'
                st.session_state.selected_style = 'casual'
        
        # Get style from session state if available
        if 'selected_style' in st.session_state:
            outfit_type = st.session_state.selected_style
        
        # ====================================================================
        # GENDER SELECTION
        # ====================================================================
        
        st.markdown("<div style='height: 2px; background: linear-gradient(90deg, #667eea 0%, transparent 100%); margin: 25px 0;'></div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); 
                    border-radius: 12px; padding: 15px; margin: 15px 0;'>
            <h3 style='margin-top: 0; color: #667eea;'>👥 Select Your Gender</h3>
            <p style='color: #666; margin: 0;'>This helps us personalize outfit recommendations</p>
        </div>
        """, unsafe_allow_html=True)
        
        gender_col1, gender_col2, gender_col3 = st.columns(3)
        
        selected_gender = None
        
        with gender_col1:
            if st.button("👨 Male", use_container_width=True, key="male_btn"):
                selected_gender = 'Male'
                st.session_state.selected_gender = 'Male'
        
        with gender_col2:
            if st.button("👩 Female", use_container_width=True, key="female_btn"):
                selected_gender = 'Female'
                st.session_state.selected_gender = 'Female'
        
        with gender_col3:
            if st.button("🤷 Other", use_container_width=True, key="other_btn"):
                selected_gender = 'Other'
                st.session_state.selected_gender = 'Other'
        
        # Get gender from session state if available
        if 'selected_gender' in st.session_state:
            selected_gender = st.session_state.selected_gender
        
        # ====================================================================
        # STEP 3: ANALYSIS & RECOMMENDATIONS
        # ====================================================================
        
        if outfit_type and selected_gender:
            st.divider()
            st.subheader("🔍 Analyzing Your Photo...")
            
            # Create progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Initialize analyzers
                analyzer = ImageAnalyzer()
                recommender = OutfitRecommender()
                
                # Load image - create cv2 image from bytes directly
                status_text.text("📥 Loading image...")
                progress_bar.progress(10)
                
                nparr = np.frombuffer(file_bytes, np.uint8)
                img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                if img_cv is None:
                    st.error("❌ Could not load image. Please try a different image.")
                    return
                
                # Analyze image
                status_text.text("🔎 Analyzing image features...")
                progress_bar.progress(30)
                
                analysis_results = analyzer.comprehensive_analysis(img_cv)
                
                # Override detected gender with user selection
                analysis_results['gender']['gender'] = selected_gender
                analysis_results['gender']['confidence'] = 1.0  # User selected, 100% confidence
                
                st.session_state.analysis_results = analysis_results
                st.session_state.selected_gender_choice = selected_gender
                
                # Generate recommendations
                status_text.text("💡 Generating outfit recommendations...")
                progress_bar.progress(60)
                
                recommendation = recommender.get_recommendations(analysis_results, outfit_type)
                st.session_state.recommendation = recommendation
                
                progress_bar.progress(100)
                status_text.text("✅ Analysis complete!")
                
                # Clear progress indicators
                time.sleep(0.5)
                progress_bar.empty()
                status_text.empty()
                
                st.success("✨ Analysis Complete! See your results below.")
                st.markdown("<div style='height: 2px; background: linear-gradient(90deg, #667eea 0%, transparent 100%); margin: 30px 0;'></div>", unsafe_allow_html=True)
                
                # ================================================================
                # DISPLAY RESULTS
                # ================================================================
                
                st.markdown("""
                <div style='text-align: center; margin: 30px 0;'>
                    <h2 style='margin: 0; font-size: 2em;'>✨ Your Personalized Outfit Results ✨</h2>
                    <p style='color: #667eea; font-size: 1.05em; margin-top: 10px;'>Explore your analysis, recommendations, and visualizations below</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Tab 1-3: Analysis, Recommendations, Amazon (preview removed)
                tab1, tab2, tab3 = st.tabs([
                    "📊 ANALYSIS", 
                    "🎀 RECOMMENDATIONS", 
                    "🛍️ AMAZON PICKS"
                ])
                
                with tab1:
                    st.markdown("""
                    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); 
                                border-radius: 12px; padding: 20px;'>
                        <h3 style='margin-top: 0; color: #667eea;'>📊 Your Feature Analysis</h3>
                        <p style='color: #666;'>Detailed breakdown of your unique features and characteristics</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Get detailed observation
                    detailed_obs = analyzer.get_detailed_observation(img_cv)
                    
                    # Display observation with better styling
                    if 'observation' in detailed_obs and detailed_obs['observation']:
                        st.markdown("""
                        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                    color: white; border-radius: 12px; padding: 20px; margin-bottom: 20px;'>
                            <h3 style='margin: 0 0 15px 0; font-size: 1.3em;'>👁️ DETAILED OBSERVATION</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        for idx, obs in enumerate(detailed_obs['observation'], 1):
                            st.markdown(f"""
                            <div style='background: white; border-left: 4px solid #667eea; padding: 12px 15px; margin: 10px 0; border-radius: 6px;'>
                                <strong style='color: #667eea;'>✓ {obs}</strong>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.markdown("<div style='height: 2px; background: linear-gradient(90deg, #667eea 0%, transparent 100%); margin: 25px 0;'></div>", unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("""
                        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                    color: white; border-radius: 12px; padding: 20px; margin-bottom: 15px;'>
                            <h3 style='margin: 0; font-size: 1.2em;'>🎯 Detected Features</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        formatted_results = format_analysis_results(analysis_results)
                        for feature, value in formatted_results.items():
                            st.markdown(f"""
                            <div style='background: white; border: 2px solid #667eea; border-radius: 8px; padding: 10px 15px; margin: 10px 0;'>
                                <strong style='color: #667eea;'>{feature}</strong><br>
                                <span style='color: #555;'>{value}</span>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("""
                        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                                    color: white; border-radius: 12px; padding: 20px; margin-bottom: 15px;'>
                            <h3 style='margin: 0; font-size: 1.2em;'>📈 Analysis Insights</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Show a simple analysis summary based on recommendation data
                        insights = []
                        if recommendation.get('colors'):
                            insights.append(f"Primary color: {recommendation['colors'].get('primary')}")
                        if recommendation.get('styles'):
                            insights.append(f"Suggested style: {recommendation['styles'].get('primary')}")
                        for insight in insights:
                            st.markdown(f"<div style='background: white; border-left: 3px solid #f5576c; padding: 8px 12px; margin: 8px 0; border-radius: 4px;'><span style='color: #333;'>{insight}</span></div>", unsafe_allow_html=True)
                
                with tab2:
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); 
                                border-radius: 12px; padding: 20px; margin-bottom: 20px;'>
                        <h3 style='margin-top: 0; color: #667eea;'>🎨 {recommendation['outfit_type'].upper()} OUTFIT RECOMMENDATIONS</h3>
                        <p style='color: #666; margin: 0;'>Personalized outfit suggestions based on your unique profile</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns([1.2, 2.8])
                    
                    with col1:
                        st.markdown("""
                        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                    color: white; border-radius: 12px; padding: 18px; margin-bottom: 15px;'>
                            <h4 style='margin: 0 0 15px 0; font-size: 1.1em;'>👤 YOUR PROFILE</h4>
                        </div>
                        """, unsafe_allow_html=True)
                        # Allow user to override detected gender if needed
                        detected_gender = analysis_results.get('gender', {}).get('gender', 'Unknown')
                        gender_options = [f"Detected: {detected_gender}", "Male", "Female", "Other"]
                        # Callback to handle gender changes and recompute recommendations immediately
                        def _on_gender_change():
                            sel = st.session_state.get('gender_select', f"Detected: {detected_gender}")
                            if isinstance(sel, str) and sel.startswith('Detected:'):
                                st.session_state['override_gender'] = detected_gender
                            else:
                                st.session_state['override_gender'] = sel
                            # Recompute recommendation if analysis and selected style exist
                            if st.session_state.get('analysis_results') and st.session_state.get('selected_style'):
                                recommender = OutfitRecommender()
                                ar = st.session_state['analysis_results']
                                ar['gender']['gender'] = st.session_state['override_gender']
                                ar['gender']['confidence'] = 1.0
                                rec = recommender.get_recommendations(ar, st.session_state['selected_style'])
                                st.session_state['recommendation'] = rec
                        # Ensure override_gender is always set
                        if 'override_gender' not in st.session_state:
                            st.session_state['override_gender'] = detected_gender
                        chosen = st.selectbox("Adjust gender for recommendations:", gender_options, index=0, key='gender_select', on_change=_on_gender_change)

                        profile_items = [
                            ("👥 Gender", st.session_state['override_gender']),
                            ("🎨 Skin Tone", recommendation.get('skin_tone', 'N/A')),
                            ("😊 Face Shape", recommendation.get('face_shape', 'N/A')),
                            ("💪 Body Type", recommendation.get('body_structure', 'N/A'))
                        ]

                        for emoji_label, value in profile_items:
                            st.markdown(f"""
                            <div style='background: white; border-left: 4px solid #667eea; padding: 10px 12px; margin: 8px 0; border-radius: 6px;'>
                                <strong style='color: #667eea;'>{emoji_label}</strong><br>
                                <span style='color: #555;'>{value}</span>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    with col2:
                        display_outfit_recommendation(recommendation)

                    # Add YouTube styling video section based on gender and outfit type
                    gender = st.session_state.get('override_gender', 'Female').lower()
                    outfit_type = st.session_state.get('selected_style', 'casual').lower()
                    youtube_links = {
                        ('male', 'western'): 'https://www.youtube.com/results?search_query=how+to+style+western+male',
                        ('male', 'casual'): 'https://www.youtube.com/results?search_query=how+to+style+casual+male',
                        ('male', 'traditional'): 'https://www.youtube.com/results?search_query=how+to+style+traditional+male',
                        ('female', 'western'): 'https://www.youtube.com/results?search_query=how+to+style+western+female',
                        ('female', 'casual'): 'https://www.youtube.com/results?search_query=how+to+style+casual+female',
                        ('female', 'traditional'): 'https://www.youtube.com/results?search_query=how+to+style+traditional+female',
                    }
                    yt_url = youtube_links.get((gender, outfit_type))
                    if yt_url:
                        st.markdown(f"""
                        <div style='margin-top: 30px; padding: 18px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 12px;'>
                            <h4 style='color: #764ba2; margin-bottom: 10px;'>🎥 How to Style {outfit_type.capitalize()} Wear for {gender.capitalize()}</h4>
                            <a href='{yt_url}' target='_blank' style='font-size: 1.1em; color: #667eea; font-weight: bold;'>
                                👉 Watch on YouTube
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                
                with tab3:
                    st.markdown("""
                    <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); 
                                border-radius: 12px; padding: 20px; margin-bottom: 20px;'>
                        <h3 style='margin-top: 0; color: #667eea;'>🛍️ SHOP THESE ITEMS ON AMAZON</h3>
                        <p style='color: #666; margin: 0;'>Handpicked items for your style - Click to view and purchase</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Get gender for Amazon suggestions (allow override from session)
                    gender = st.session_state.get('override_gender', analysis_results.get('gender', {}).get('gender', 'Female'))
                    suggestions = AmazonSuggestions.get_suggestions(gender, outfit_type)
                    
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #FF9900 0%, #FF6B35 100%); 
                                color: white; border-radius: 10px; padding: 15px; margin-bottom: 20px; text-align: center;'>
                        <strong style='font-size: 1.1em;'>👕 Personalized items for {gender.lower()} - {outfit_type.capitalize()} STYLE</strong>
                        <div style='font-size:0.85em; opacity:0.95; margin-top:6px;'>Using gender: <strong>{gender}</strong></div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display products in columns
                    cols = st.columns(2)
                    for idx, product in enumerate(suggestions['products']):
                        with cols[idx % 2]:
                            st.markdown(f"""
                            <div style='background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%); 
                                        border: 2px solid #FF9900; border-radius: 12px; padding: 18px; margin: 12px 0;
                                        box-shadow: 0 4px 12px rgba(255, 153, 0, 0.15); transition: all 0.3s ease;'>
                                <h4 style='margin: 0 0 10px 0; color: #333; font-size: 1.1em;'>🛒 {product['name']}</h4>
                                <p style='margin: 8px 0; color: #666;'><strong>Available Colors:</strong></p>
                                <div style='display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;'>
                                    {', '.join([f"<span style=\"background: #f0f0f0; color: #333; padding: 4px 10px; border-radius: 12px; font-size: 0.9em;\">{color}</span>" for color in product['colors']])}
                                </div>
                                <a href='{product['link']}' target='_blank' style='
                                    display: inline-block;
                                    background: linear-gradient(135deg, #FF9900 0%, #FF6B35 100%);
                                    color: white;
                                    padding: 10px 20px;
                                    border-radius: 8px;
                                    text-decoration: none;
                                    font-weight: bold;
                                    box-shadow: 0 4px 8px rgba(255, 107, 53, 0.3);
                                    transition: all 0.3s ease;
                                '>✨ View on Amazon</a>
                            </div>
                            """, unsafe_allow_html=True)
                
                    
                    st.markdown("<div style='height: 2px; background: linear-gradient(90deg, #667eea 0%, transparent 100%); margin: 25px 0;'></div>", unsafe_allow_html=True)
                    
                    # More style options
                    # Removed alternative outfit generation. Only one preview is shown.
                
                st.markdown("<div style='height: 3px; background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #667eea 100%); border-radius: 2px; margin: 30px 0;'></div>", unsafe_allow_html=True)
                
                # ================================================================
                # ACTION BUTTONS
                # ================================================================
                
                st.markdown("""
                <div style='text-align: center; margin: 25px 0;'>
                    <h3 style='color: #667eea; margin-bottom: 20px;'>⚡ QUICK ACTIONS</h3>
                </div>
                """, unsafe_allow_html=True)
                
                col_save, col_new = st.columns(2)
                
                with col_save:
                    if st.button("💾 Save Results", use_container_width=True):
                        st.markdown("""
                        <div style='background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); 
                                    color: #155724; border-radius: 10px; padding: 12px; text-align: center;'>
                            ✅ Results saved locally in session. (File export feature available in premium version)
                        </div>
                        """, unsafe_allow_html=True)
                
                with col_new:
                    if st.button("🔄 Try Another Image", use_container_width=True):
                        st.session_state.analysis_results = None
                        st.session_state.recommendation = None
                        st.session_state.rating_result = None
                        st.rerun()
            
            except Exception as e:
                st.error(f"❌ An error occurred during analysis: {str(e)}")
                st.info("💡 Try with a clearer image or check that all features are visible.")
    
    else:
        # Display welcome message when no image is uploaded
        st.info("""
        ### 👋 Welcome to AI Outfit Recommendation System!
        
        **How it works:**
        1. **Upload** a clear photo of yourself
        2. **Choose** your preferred outfit style (Traditional, Western, or Casual)
        3. **Get** personalized recommendations based on your features
        4. **Receive** a rating and styling tips
        
        **Features:**
        - 🔍 Advanced image analysis using AI
        - 🎨 Personalized color and style recommendations
        - ⭐ Look rating with compliments
        - 💡 Detailed styling tips
        
        **Privacy:**
        - Your images are not stored permanently
        - Analysis happens locally
        - No data is shared
        """)

if __name__ == "__main__":
    import time
    main()
