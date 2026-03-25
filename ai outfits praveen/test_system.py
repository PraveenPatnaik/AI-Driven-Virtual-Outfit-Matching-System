"""
Test Script for AI Outfit Recommendation System
Verify all modules work correctly before running the web app
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test if all modules can be imported"""
    print("\n" + "="*60)
    print("TESTING MODULE IMPORTS")
    print("="*60)
    
    try:
        print("Testing image_analysis.py...", end=" ")
        from src.image_analysis import ImageAnalyzer
        print("✓")
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    try:
        print("Testing outfit_recommender.py...", end=" ")
        from src.outfit_recommender import OutfitRecommender
        print("✓")
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    try:
        print("Testing rating_logic.py...", end=" ")
        from src.rating_logic import LookRating
        print("✓")
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    try:
        print("Testing constants.py...", end=" ")
        from src.constants import OUTFIT_TYPES, SKIN_TONES
        print("✓")
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    try:
        print("Testing utils.py...", end=" ")
        from src.utils import setup_logger, get_confidence_level
        print("✓")
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    return True

def test_analyzer_instantiation():
    """Test if ImageAnalyzer can be instantiated"""
    print("\n" + "="*60)
    print("TESTING IMAGEANALYZER INSTANTIATION")
    print("="*60)
    
    try:
        from src.image_analysis import ImageAnalyzer
        print("Creating ImageAnalyzer instance...", end=" ")
        analyzer = ImageAnalyzer()
        print("✓")
        print(f"  - Face detector initialized: {analyzer.face_detector is not None}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_recommender_instantiation():
    """Test if OutfitRecommender can be instantiated"""
    print("\n" + "="*60)
    print("TESTING OUTFIT RECOMMENDER INSTANTIATION")
    print("="*60)
    
    try:
        from src.outfit_recommender import OutfitRecommender
        print("Creating OutfitRecommender instance...", end=" ")
        recommender = OutfitRecommender()
        print("✓")
        print(f"  - Number of outfit types: {len(recommender.outfit_types)}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_rating_instantiation():
    """Test if LookRating can be instantiated"""
    print("\n" + "="*60)
    print("TESTING LOOK RATING INSTANTIATION")
    print("="*60)
    
    try:
        from src.rating_logic import LookRating
        print("Creating LookRating instance...", end=" ")
        rater = LookRating()
        print("✓")
        print(f"  - Max rating: {rater.max_rating}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_constants_data():
    """Test if constants are properly loaded"""
    print("\n" + "="*60)
    print("TESTING CONSTANTS DATA")
    print("="*60)
    
    try:
        from src.constants import (
            OUTFIT_TYPES, SKIN_TONES, FACE_SHAPES,
            OUTFIT_RECOMMENDATIONS, COMPLIMENTS
        )
        
        print(f"Outfit types: {len(OUTFIT_TYPES)} - {list(OUTFIT_TYPES.keys())}")
        print(f"Skin tones: {len(SKIN_TONES)} - {list(SKIN_TONES.keys())}")
        print(f"Face shapes: {len(FACE_SHAPES)} - {list(FACE_SHAPES.keys())}")
        
        # Verify recommendation database
        print("\nVerifying outfit recommendation database:")
        for outfit_type in OUTFIT_TYPES.keys():
            for skin_tone in SKIN_TONES.keys():
                data = OUTFIT_RECOMMENDATIONS.get(outfit_type, {}).get(skin_tone, {})
                if data:
                    print(f"  ✓ {outfit_type}/{skin_tone}: {len(data.get('colors', []))} colors, {len(data.get('styles', []))} styles")
                else:
                    print(f"  ✗ Missing data for {outfit_type}/{skin_tone}")
                    return False
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_mock_analysis():
    """Test the analysis workflow with mock data"""
    print("\n" + "="*60)
    print("TESTING MOCK ANALYSIS WORKFLOW")
    print("="*60)
    
    try:
        from src.outfit_recommender import OutfitRecommender
        from src.rating_logic import LookRating
        
        # Create mock analysis results
        mock_analysis = {
            'skin_tone': {'tone': 'medium', 'confidence': 0.85},
            'face_shape': {'shape': 'oval', 'confidence': 0.80},
            'body_structure': {'structure': 'average', 'confidence': 0.75},
            'image_quality': {'score': 0.80}
        }
        
        print("Mock analysis data created:")
        print(f"  - Skin tone: {mock_analysis['skin_tone']['tone']}")
        print(f"  - Face shape: {mock_analysis['face_shape']['shape']}")
        print(f"  - Body structure: {mock_analysis['body_structure']['structure']}")
        
        # Test recommendation
        print("\nGenerating recommendations...", end=" ")
        recommender = OutfitRecommender()
        recommendation = recommender.get_recommendations(mock_analysis, 'traditional')
        print("✓")
        
        if 'error' not in recommendation:
            print(f"  - Outfit type: {recommendation.get('outfit_type', 'N/A')}")
            print(f"  - Primary color: {recommendation.get('colors', {}).get('primary', 'N/A')}")
            print(f"  - Primary style: {recommendation.get('styles', {}).get('primary', 'N/A')}")
            print(f"  - Confidence: {recommendation.get('confidence', 0)}")
        else:
            print(f"  Error: {recommendation['error']}")
            return False
        
        # Test rating
        print("\nGenerating rating...", end=" ")
        rater = LookRating()
        rating = rater.rate_look(mock_analysis, recommendation, 'traditional')
        print("✓")
        
        print(f"  - Rating: {rating.get('numeric_rating', 0)}/10")
        print(f"  - Star rating: {rating.get('star_rating', 'N/A')}")
        print(f"  - Compliment: {rating.get('compliment', 'N/A')}")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_utilities():
    """Test utility functions"""
    print("\n" + "="*60)
    print("TESTING UTILITY FUNCTIONS")
    print("="*60)
    
    try:
        from src.utils import (
            get_confidence_level, format_percentage, format_label,
            is_valid_rating, is_valid_outfit_type, is_valid_skin_tone
        )
        
        print("Testing confidence level conversion:")
        print(f"  - 0.9 -> {get_confidence_level(0.9)}")
        print(f"  - 0.5 -> {get_confidence_level(0.5)}")
        
        print("\nTesting percentage formatting:")
        print(f"  - 0.75 -> {format_percentage(0.75)}")
        
        print("\nTesting label formatting:")
        print(f"  - 'face_shape' -> {format_label('face_shape')}")
        
        print("\nTesting validation functions:")
        print(f"  - is_valid_rating(7): {is_valid_rating(7)}")
        print(f"  - is_valid_rating(15): {is_valid_rating(15)}")
        print(f"  - is_valid_outfit_type('traditional'): {is_valid_outfit_type('traditional')}")
        print(f"  - is_valid_skin_tone('medium'): {is_valid_skin_tone('medium')}")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  AI OUTFIT RECOMMENDATION SYSTEM - TEST SUITE  ".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    tests = [
        ("Module Imports", test_imports),
        ("ImageAnalyzer Instantiation", test_analyzer_instantiation),
        ("OutfitRecommender Instantiation", test_recommender_instantiation),
        ("LookRating Instantiation", test_rating_instantiation),
        ("Constants Data", test_constants_data),
        ("Mock Analysis Workflow", test_mock_analysis),
        ("Utility Functions", test_utilities),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            result = test_func()
            results[test_name] = result
        except Exception as e:
            print(f"\n✗ Unexpected error in {test_name}: {e}")
            results[test_name] = False
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {test_name}")
    
    print("="*60)
    print(f"TOTAL: {passed}/{total} tests passed")
    print("="*60)
    
    if passed == total:
        print("\n🎉 All tests passed! System is ready to use.")
        print("\nTo start the application, run:")
        print("  streamlit run app.py")
        return True
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
