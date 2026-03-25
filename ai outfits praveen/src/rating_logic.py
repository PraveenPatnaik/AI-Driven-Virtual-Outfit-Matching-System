"""
Look Rating System
Rates the final outfit look based on analysis and recommendations
"""

from constants import RATING_DESCRIPTIONS, COMPLIMENTS
import random


class LookRating:
    """
    Generates a rating (1-10) for the outfit combination
    Provides star rating, numeric rating, and personalized compliments
    """
    
    def __init__(self):
        """Initialize the rating system"""
        self.max_rating = 10
    
    def rate_look(self, analysis_results, recommendation, outfit_type):
        """
        Rate the outfit based on all factors
        
        Args:
            analysis_results: Dictionary from ImageAnalyzer.comprehensive_analysis()
            recommendation: Dictionary from OutfitRecommender.get_recommendations()
            outfit_type: User's chosen outfit type
            
        Returns:
            Dictionary with rating details and compliments
        """
        try:
            # Calculate rating based on multiple factors
            rating = self._calculate_rating(analysis_results, recommendation, outfit_type)
            
            # Generate rating details
            rating_result = {
                'numeric_rating': rating,
                'star_rating': self._get_star_rating(rating),
                'description': self._get_description(rating),
                'compliment': self._get_compliment(rating),
                'breakdown': self._get_rating_breakdown(analysis_results, recommendation),
                'recommendations_to_improve': self._get_improvement_tips(rating, outfit_type)
            }
            
            return rating_result
        
        except Exception as e:
            return {
                'numeric_rating': 5,
                'star_rating': '⭐⭐⭐⭐⭐',
                'description': 'Neutral rating',
                'compliment': 'Keep exploring and experimenting!',
                'error': str(e)
            }
    
    def _calculate_rating(self, analysis_results, recommendation, outfit_type):
        """
        Calculate numeric rating (1-10) based on multiple factors
        
        Args:
            analysis_results: Image analysis results
            recommendation: Outfit recommendations
            outfit_type: Outfit type chosen
            
        Returns:
            Integer rating (1-10)
        """
        base_score = 5.0  # Start with neutral rating
        
        # Factor 1: Image Analysis Quality (up to +2 points)
        image_quality = analysis_results.get('image_quality', {}).get('score', 0.5)
        base_score += image_quality * 2
        
        # Factor 2: Analysis Confidence (up to +1.5 points)
        skin_confidence = analysis_results.get('skin_tone', {}).get('confidence', 0.5)
        face_confidence = analysis_results.get('face_shape', {}).get('confidence', 0.5)
        avg_analysis_confidence = (skin_confidence + face_confidence) / 2
        base_score += avg_analysis_confidence * 1.5
        
        # Factor 3: Recommendation Confidence (up to +1 point)
        rec_confidence = recommendation.get('confidence', 0.5)
        base_score += rec_confidence * 1
        
        # Factor 4: Body-Outfit Type Match (up to +0.5 points)
        body_structure = analysis_results.get('body_structure', {}).get('structure', 'average')
        base_score += self._get_body_outfit_match(body_structure, outfit_type) * 0.5
        
        # Ensure rating is between 1 and 10
        final_rating = max(1, min(10, round(base_score)))
        
        return final_rating
    
    def _get_body_outfit_match(self, body_structure, outfit_type):
        """
        Rate how well body structure matches chosen outfit type
        
        Args:
            body_structure: Body type (slim, average, athletic)
            outfit_type: Outfit type (traditional, western, casual)
            
        Returns:
            Match score (0-1)
        """
        match_matrix = {
            ('slim', 'traditional'): 0.95,      # Excellent match
            ('slim', 'western'): 0.85,
            ('slim', 'casual'): 0.90,
            ('average', 'traditional'): 0.90,
            ('average', 'western'): 0.95,
            ('average', 'casual'): 0.95,
            ('athletic', 'traditional'): 0.85,
            ('athletic', 'western'): 0.95,
            ('athletic', 'casual'): 0.90,
        }
        
        return match_matrix.get((body_structure, outfit_type), 0.75)
    
    def _get_star_rating(self, numeric_rating):
        """
        Convert numeric rating to star representation
        
        Args:
            numeric_rating: Rating from 1-10
            
        Returns:
            String with star emojis
        """
        full_stars = int(numeric_rating / 2)
        remaining = numeric_rating % 2
        
        stars = '⭐' * full_stars
        
        if remaining >= 1:
            stars += '✨'
        
        return stars
    
    def _get_description(self, rating):
        """
        Get description based on rating
        
        Args:
            rating: Numeric rating (1-10)
            
        Returns:
            Description string
        """
        for range_tuple, description in RATING_DESCRIPTIONS.items():
            if range_tuple[0] <= rating <= range_tuple[1]:
                return description
        
        return "Great look!"
    
    def _get_compliment(self, rating):
        """
        Get a personalized compliment based on rating
        
        Args:
            rating: Numeric rating (1-10)
            
        Returns:
            Compliment string
        """
        for range_tuple, compliments_list in COMPLIMENTS.items():
            if range_tuple[0] <= rating <= range_tuple[1]:
                return random.choice(compliments_list)
        
        return "You're looking great!"
    
    def _get_rating_breakdown(self, analysis_results, recommendation):
        """
        Provide detailed breakdown of what influenced the rating
        
        Args:
            analysis_results: Image analysis results
            recommendation: Outfit recommendations
            
        Returns:
            Dictionary with rating factors
        """
        breakdown = {
            'image_quality': {
                'score': analysis_results.get('image_quality', {}).get('score', 0.5),
                'factor': 'Image clarity and lighting quality'
            },
            'skin_tone_analysis': {
                'detected': analysis_results.get('skin_tone', {}).get('tone', 'unknown'),
                'confidence': analysis_results.get('skin_tone', {}).get('confidence', 0),
                'factor': 'Accuracy of skin tone detection'
            },
            'face_shape_analysis': {
                'detected': analysis_results.get('face_shape', {}).get('shape', 'unknown'),
                'confidence': analysis_results.get('face_shape', {}).get('confidence', 0),
                'factor': 'Accuracy of face shape detection'
            },
            'body_structure_analysis': {
                'detected': analysis_results.get('body_structure', {}).get('structure', 'unknown'),
                'confidence': analysis_results.get('body_structure', {}).get('confidence', 0),
                'factor': 'Body structure estimation accuracy'
            },
            'outfit_match': {
                'recommendation_confidence': recommendation.get('confidence', 0),
                'factor': 'How well outfit matches your features'
            }
        }
        
        return breakdown
    
    def _get_improvement_tips(self, rating, outfit_type):
        """
        Provide tips based on current rating
        
        Args:
            rating: Current numeric rating
            outfit_type: Chosen outfit type
            
        Returns:
            List of improvement suggestions
        """
        tips = {
            (1, 3): [
                'Try taking a photo with better lighting',
                'Ensure your face is clearly visible to camera',
                'Consider different outfit styles for better match',
                'Experiment with different color combinations'
            ],
            (4, 5): [
                'Add statement accessories to enhance the look',
                'Try better lighting for your photoshoot',
                'Consider fabric quality and fit',
                'Experiment with different necklines'
            ],
            (6, 7): [
                'Perfect! Minor adjustments could make it even better',
                'Try adding a complementary layer or accessory',
                'Consider shoes that match your outfit theme',
                'Play with different makeup or grooming styles'
            ],
            (8, 9): [
                'Excellent choice! You\'ve got great style sense',
                'Consider minor tweaks to accessories for polish',
                'Your combination is nearly perfect',
                'Confidence is the final touch - wear it well!'
            ],
            (10, 10): [
                'You\'ve achieved a stunning look!',
                'Your style coordination is impeccable',
                'This is your signature look - own it!',
                'You\'re a fashion inspiration!'
            ]
        }
        
        # Find appropriate tips based on rating
        for range_tuple, tip_list in tips.items():
            if range_tuple[0] <= rating <= range_tuple[1]:
                return tip_list
        
        return ['Keep exploring different styles and combinations!']
