"""
Outfit Recommendation Engine
Generates outfit recommendations based on image analysis and outfit type preference
"""

from constants import OUTFIT_RECOMMENDATIONS, OUTFIT_TYPES, SKIN_TONES
import random


class OutfitRecommender:
    """
    Recommends outfits based on image analysis and user preferences
    Uses rule-based logic for outfit suggestions
    """
    
    def __init__(self):
        """Initialize the recommender"""
        self.outfit_types = OUTFIT_TYPES
        self.recommendations_db = OUTFIT_RECOMMENDATIONS
    
    def get_recommendations(self, analysis_results, outfit_type):
        """
        Generate outfit recommendations
        
        Args:
            analysis_results: Dictionary from ImageAnalyzer.comprehensive_analysis()
            outfit_type: String - 'traditional', 'western', or 'casual'
            
        Returns:
            Dictionary with outfit recommendations
        """
        try:
            # Extract key features
            skin_tone = analysis_results['skin_tone']['tone']
            face_shape = analysis_results['face_shape']['shape']
            body_structure = analysis_results['body_structure']['structure']
            
            # Validate outfit type
            if outfit_type not in self.outfit_types:
                return {'error': f'Invalid outfit type: {outfit_type}'}
            
            # Get base recommendations from database
            base_rec = self.recommendations_db[outfit_type][skin_tone]

            # Adjust base recommendations based on detected/user-selected gender
            gender = analysis_results.get('gender', {}).get('gender', '').lower()
            # Provide male-specific traditional/western/casual styles when gender is male
            if gender == 'male':
                if outfit_type == 'traditional':
                    base_rec = {
                        'colors': base_rec.get('colors', []),
                        'styles': ['Kurta', 'Dhoti/Pajama', 'Embroidered Jacket'],
                        'accessories': ['Mojari Shoes', 'Stole/Scarf', 'Brooch']
                    }
                elif outfit_type == 'western':
                    base_rec = {
                        'colors': base_rec.get('colors', []),
                        'styles': ['Blazer', 'Coat', 'Button-Down Shirt', 'Chinos'],
                        'accessories': ['Watch', 'Belt', 'Loafers']
                    }
                elif outfit_type == 'casual':
                    base_rec = {
                        'colors': base_rec.get('colors', []),
                        'styles': ['T-Shirt', 'Shorts', 'Casual Sneakers'],
                        'accessories': ['Cap', 'Sneakers', 'Backpack']
                    }
            # Provide female-specific traditional/western/casual styles when gender is female
            elif gender == 'female':
                if outfit_type == 'traditional':
                    base_rec = {
                        'colors': base_rec.get('colors', []),
                        'styles': ['Saree', 'Lehenga', 'Anarkali Suit'],
                        'accessories': ['Bangles', 'Embellished Heels', 'Clutch']
                    }
                elif outfit_type == 'western':
                    base_rec = {
                        'colors': base_rec.get('colors', []),
                        'styles': ['Blazer', 'Midi Dress', 'Trench Coat', 'Blouse'],
                        'accessories': ['Heels', 'Statement Necklace', 'Handbag']
                    }
                elif outfit_type == 'casual':
                    base_rec = {
                        'colors': base_rec.get('colors', []),
                        'styles': ['Casual Blouse', 'Jeans', 'Casual Sneakers', 'Leggings'],
                        'accessories': ['Crossbody Bag', 'Sneakers', 'Sunglasses']
                    }
            
            # Generate customized recommendations
            recommendation = {
                'outfit_type': self.outfit_types[outfit_type],
                'skin_tone': SKIN_TONES.get(skin_tone, skin_tone),
                'face_shape': face_shape.capitalize(),
                'body_structure': body_structure.capitalize(),
                'colors': self._select_colors(base_rec['colors'], face_shape),
                'styles': self._select_styles(base_rec['styles'], body_structure, outfit_type),
                'accessories': self._select_accessories(
                    base_rec['accessories'],
                    face_shape,
                    body_structure,
                    outfit_type
                ),
                'tips': self._generate_styling_tips(face_shape, body_structure, outfit_type),
                'confidence': self._calculate_confidence(analysis_results)
            }
            
            return recommendation
        
        except Exception as e:
            return {'error': f'Recommendation generation failed: {str(e)}'}
    
    def _select_colors(self, color_options, face_shape):
        """
        Select optimal colors based on face shape
        
        Args:
            color_options: List of color suggestions
            face_shape: Detected face shape
            
        Returns:
            Prioritized list of color recommendations
        """
        # Create prioritized color selection based on face shape
        face_shape_color_map = {
            'round': {
                'priority': ['Deep Gold', 'Royal Blue', 'Emerald Green', 'Wine Red'],
                'reasoning': 'Bold colors add definition'
            },
            'oval': {
                'priority': ['Pastel Pink', 'Soft Blue', 'Light Gold', 'Cream'],
                'reasoning': 'Complements well with balanced features'
            },
            'square': {
                'priority': ['Soft colors', 'Earth Tones', 'Warm Tones'],
                'reasoning': 'Softer colors balance angular features'
            },
            'heart': {
                'priority': ['Deep Colors', 'Rich Tones'],
                'reasoning': 'Rich colors highlight your features'
            },
            'oblong': {
                'priority': ['Horizontal patterns', 'Bold Colors'],
                'reasoning': 'Adds width and balance'
            }
        }
        
        selected_colors = color_options[:3]  # Return top 3 colors
        reasoning = face_shape_color_map.get(face_shape, {}).get('reasoning', '')
        
        return {
            'primary': selected_colors[0] if selected_colors else 'Classic Tones',
            'secondary': selected_colors[1] if len(selected_colors) > 1 else 'Neutral',
            'accent': selected_colors[2] if len(selected_colors) > 2 else 'Coordinating',
            'reasoning': reasoning
        }
    
    def _select_styles(self, style_options, body_structure, outfit_type):
        """
        Select appropriate styles based on body structure
        
        Args:
            style_options: List of style suggestions
            body_structure: Body structure estimation
            outfit_type: Type of outfit
            
        Returns:
            Tailored style recommendations
        """
        style_considerations = {
            'slim': {
                'traditional': 'Layered designs add volume and dimension',
                'western': 'Fitted styles with patterns create visual interest',
                'casual': 'Comfortable fits with texture and detail'
            },
            'average': {
                'traditional': 'Classic designs that highlight your balance',
                'western': 'Tailored fits that enhance your natural proportions',
                'casual': 'Versatile styles that work for any occasion'
            },
            'athletic': {
                'traditional': 'Structured designs that complement your build',
                'western': 'Fitted silhouettes that accentuate your form',
                'casual': 'Modern cuts that showcase your physique'
            }
        }
        
        primary_style = style_options[0] if style_options else 'Classic Style'
        secondary_style = style_options[1] if len(style_options) > 1 else 'Complementary Style'
        consideration = style_considerations.get(body_structure, {}).get(outfit_type, '')
        
        return {
            'primary': primary_style,
            'secondary': secondary_style,
            'consideration': consideration,
            'fit_recommendation': f'Recommended for your {body_structure} body type'
        }
    
    def _select_accessories(self, accessory_options, face_shape, body_structure, outfit_type):
        """
        Select accessories based on face shape and body structure
        
        Args:
            accessory_options: List of available accessories
            face_shape: Detected face shape
            body_structure: Body structure
            outfit_type: Type of outfit
            
        Returns:
            Recommended accessories
        """
        accessory_rules = {
            'round': {
                'avoid': 'Circular earrings that might emphasize face shape',
                'prefer': 'Geometric or elongated accessories'
            },
            'oval': {
                'prefer': 'Any style works well with balanced features',
                'avoid': 'Nothing specific - versatile face shape'
            },
            'square': {
                'avoid': 'Heavy, boxy accessories',
                'prefer': 'Softer, rounded accessories'
            },
            'heart': {
                'avoid': 'Top-heavy statement pieces',
                'prefer': 'Drop earrings and lower neckline accessories'
            },
            'oblong': {
                'avoid': 'Long, drooping accessories',
                'prefer': 'Shorter, broader pieces'
            }
        }
        
        selected = accessory_options[:2]
        rules = accessory_rules.get(face_shape, {})
        
        return {
            'recommended': selected,
            'styling_note': rules.get('prefer', 'Accessorize based on personal preference'),
            'avoid': rules.get('avoid', '')
        }
    
    def _generate_styling_tips(self, face_shape, body_structure, outfit_type):
        """
        Generate personalized styling tips
        
        Args:
            face_shape: Face shape type
            body_structure: Body structure type
            outfit_type: Outfit type
            
        Returns:
            List of styling tips
        """
        tips = [
            f"Your {face_shape} face shape pairs well with {self._get_neckline_suggestion(face_shape)}",
            f"For your {body_structure} build, focus on {self._get_fit_focus(body_structure)}",
            f"Consider layering for added depth and dimension",
            f"Ensure good lighting when wearing your chosen colors",
            f"Confidence is your best accessory - wear it with pride!"
        ]
        
        return tips
    
    def _get_neckline_suggestion(self, face_shape):
        """Get neckline suggestions based on face shape"""
        neckline_map = {
            'round': 'v-necks or vertical patterns',
            'oval': 'any neckline style',
            'square': 'round or soft necklines',
            'heart': 'strapless or sweetheart necklines',
            'oblong': 'horizontal stripes or wide necklines'
        }
        return neckline_map.get(face_shape, 'your preferred style')
    
    def _get_fit_focus(self, body_structure):
        """Get fit focus based on body structure"""
        fit_map = {
            'slim': 'layering and textured fabrics',
            'average': 'tailored fits that complement your proportions',
            'athletic': 'styles that showcase your toned physique'
        }
        return fit_map.get(body_structure, 'balanced proportions')
    
    def _calculate_confidence(self, analysis_results):
        """
        Calculate overall confidence of recommendations
        Based on quality of image analysis
        
        Args:
            analysis_results: Analysis results dictionary
            
        Returns:
            Confidence score (0-1)
        """
        try:
            skin_confidence = analysis_results.get('skin_tone', {}).get('confidence', 0.5)
            face_confidence = analysis_results.get('face_shape', {}).get('confidence', 0.5)
            body_confidence = analysis_results.get('body_structure', {}).get('confidence', 0.5)
            quality_score = analysis_results.get('image_quality', {}).get('score', 0.5)
            
            # Average confidence with weight towards image quality
            avg_confidence = (skin_confidence + face_confidence + body_confidence) / 3
            final_confidence = (avg_confidence * 0.7) + (quality_score * 0.3)
            
            return round(final_confidence, 2)
        
        except Exception as e:
            return 0.6
