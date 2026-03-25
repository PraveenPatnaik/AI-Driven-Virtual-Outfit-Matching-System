"""
Outfit Visualizer Module
Generates visual representations of recommended outfits
"""

from PIL import Image, ImageDraw, ImageFont
import io
import numpy as np


class OutfitVisualizer:
    """Generate outfit visualizations and mockups"""
    
    def __init__(self):
        self.outfit_colors = {
            'light': {
                'skin': (255, 220, 177),
                'face': (255, 200, 150),
                'hair_light': (200, 160, 120),
                'hair_dark': (120, 80, 40),
            },
            'medium': {
                'skin': (210, 150, 120),
                'face': (200, 130, 90),
                'hair_light': (100, 70, 40),
                'hair_dark': (60, 35, 10),
            },
            'dark': {
                'skin': (140, 90, 60),
                'face': (120, 70, 40),
                'hair_light': (60, 40, 20),
                'hair_dark': (30, 20, 10),
            }
        }
        
        self.outfit_colors_map = {
            'black': (30, 30, 30),
            'navy': (25, 50, 100),
            'gray': (128, 128, 128),
            'white': (255, 255, 255),
            'brown': (139, 69, 19),
            'red': (220, 20, 60),
            'blue': (30, 144, 255),
            'green': (34, 139, 34),
            'pink': (255, 192, 203),
            'gold': (255, 215, 0),
            'tan': (210, 180, 140),
            'burgundy': (128, 0, 32),
        }
    
    def create_outfit_mockup(self, recommendation, skin_tone='medium', gender='Male'):
        """
        Create a visual mockup of the recommended outfit
        
        Args:
            recommendation: Outfit recommendation dict
            skin_tone: 'light', 'medium', or 'dark'
            gender: 'Male' or 'Female'
            
        Returns:
            PIL Image of the outfit mockup
        """
        # Create canvas
        width, height = 400, 600
        image = Image.new('RGB', (width, height), color=(240, 245, 250))
        draw = ImageDraw.Draw(image)
        
        # Get skin tone colors
        colors = self.outfit_colors.get(skin_tone, self.outfit_colors['medium'])
        
        # Draw person silhouette
        if gender == 'Male':
            self._draw_male_figure(draw, colors, width, height, recommendation)
        else:
            self._draw_female_figure(draw, colors, width, height, recommendation)
        
        # Add outfit details
        self._add_outfit_details(draw, image, recommendation, width, height)
        
        return image
    
    def _draw_male_figure(self, draw, colors, width, height, recommendation):
        """Draw male figure with outfit"""
        # Head
        head_pos = [(width//2 - 40, 40), (width//2 + 40, 120)]
        draw.ellipse(head_pos, fill=colors['face'], outline=(100, 100, 100), width=2)
        
        # Hair
        hair_pos = [(width//2 - 45, 30), (width//2 + 45, 100)]
        draw.ellipse(hair_pos, fill=colors['hair_dark'])
        
        # Eyes
        eye_y = 70
        draw.ellipse([(width//2 - 25, eye_y), (width//2 - 15, eye_y + 10)], fill=(0, 0, 0))
        draw.ellipse([(width//2 + 15, eye_y), (width//2 + 25, eye_y + 10)], fill=(0, 0, 0))
        
        # Neck
        draw.rectangle([(width//2 - 15, 110), (width//2 + 15, 140)], fill=colors['skin'])
        
        # Torso (Shirt)
        shirt_color = self._get_color(recommendation.get('primary_color', 'navy'))
        torso_top = 140
        torso_height = 150
        draw.rectangle([(width//2 - 60, torso_top), (width//2 + 60, torso_top + torso_height)], 
                       fill=shirt_color, outline=(50, 50, 50), width=2)
        
        # Arms
        arm_color = colors['skin']
        draw.rectangle([(width//2 - 70, torso_top + 20), (width//2 - 60, torso_top + 120)], 
                       fill=arm_color)  # Left arm
        draw.rectangle([(width//2 + 60, torso_top + 20), (width//2 + 70, torso_top + 120)], 
                       fill=arm_color)  # Right arm
        
        # Pants
        pants_color = self._get_color(recommendation.get('secondary_color', 'black'))
        pants_top = torso_top + torso_height
        draw.rectangle([(width//2 - 60, pants_top), (width//2 + 60, pants_top + 120)], 
                       fill=pants_color, outline=(50, 50, 50), width=2)
        
        # Shoes
        shoe_color = self._get_color(recommendation.get('shoe_color', 'black'))
        draw.rectangle([(width//2 - 35, pants_top + 120), (width//2 - 5, height - 20)], 
                       fill=shoe_color)  # Left shoe
        draw.rectangle([(width//2 + 5, pants_top + 120), (width//2 + 35, height - 20)], 
                       fill=shoe_color)  # Right shoe
    
    def _draw_female_figure(self, draw, colors, width, height, recommendation):
        """Draw female figure with outfit"""
        # Head
        head_pos = [(width//2 - 40, 50), (width//2 + 40, 130)]
        draw.ellipse(head_pos, fill=colors['face'], outline=(100, 100, 100), width=2)
        
        # Hair
        hair_pos = [(width//2 - 50, 40), (width//2 + 50, 120)]
        draw.ellipse(hair_pos, fill=colors['hair_dark'])
        
        # Eyes
        eye_y = 80
        draw.ellipse([(width//2 - 25, eye_y), (width//2 - 15, eye_y + 10)], fill=(0, 0, 0))
        draw.ellipse([(width//2 + 15, eye_y), (width//2 + 25, eye_y + 10)], fill=(0, 0, 0))
        
        # Lips
        draw.ellipse([(width//2 - 12, eye_y + 20), (width//2 + 12, eye_y + 28)], fill=(200, 100, 100))
        
        # Neck
        draw.rectangle([(width//2 - 15, 120), (width//2 + 15, 145)], fill=colors['skin'])
        
        # Dress/Top
        dress_color = self._get_color(recommendation.get('primary_color', 'navy'))
        dress_top = 145
        draw.polygon([(width//2 - 70, dress_top), (width//2 + 70, dress_top),
                      (width//2 + 60, dress_top + 200), (width//2 - 60, dress_top + 200)],
                     fill=dress_color, outline=(50, 50, 50))
        
        # Arms
        arm_color = colors['skin']
        draw.ellipse([(width//2 - 80, dress_top + 10), (width//2 - 70, dress_top + 100)], 
                     fill=arm_color)  # Left arm
        draw.ellipse([(width//2 + 70, dress_top + 10), (width//2 + 80, dress_top + 100)], 
                     fill=arm_color)  # Right arm
        
        # Shoes
        shoe_color = self._get_color(recommendation.get('shoe_color', 'black'))
        draw.ellipse([(width//2 - 35, height - 40), (width//2 - 5, height - 10)], 
                     fill=shoe_color)  # Left shoe
        draw.ellipse([(width//2 + 5, height - 40), (width//2 + 35, height - 10)], 
                     fill=shoe_color)  # Right shoe
    
    def _get_color(self, color_name):
        """Get RGB color from name"""
        return self.outfit_colors_map.get(color_name.lower(), (100, 100, 150))
    
    def _add_outfit_details(self, draw, image, recommendation, width, height):
        """Add text details about the outfit"""
        # Create a font (use default if TTF unavailable)
        try:
            title_font = ImageFont.truetype("arial.ttf", 16)
            text_font = ImageFont.truetype("arial.ttf", 12)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Add recommendation text below figure
        text_y = height - 120
        
        # Title
        draw.text((width//2, text_y), "Recommended Outfit", fill=(0, 0, 0), 
                 font=title_font, anchor="mm")
        
        # Details
        details = [
            f"Style: {recommendation.get('outfit_type', 'Casual').capitalize()}",
            f"Primary: {recommendation.get('primary_color', 'Navy')}",
            f"Secondary: {recommendation.get('secondary_color', 'Black')}",
            f"Accessories: {', '.join(recommendation.get('accessories', [])[:2])}"
        ]
        
        y_offset = text_y + 30
        for detail in details:
            draw.text((20, y_offset), detail, fill=(50, 50, 50), font=text_font)
            y_offset += 20
    
    def generate_outfit_image(self, analysis, recommendation, gender='Male'):
        """
        Generate complete outfit visualization
        
        Args:
            analysis: Image analysis results
            recommendation: Outfit recommendation
            gender: 'Male' or 'Female'
            
        Returns:
            PIL Image
        """
        skin_tone = analysis['skin_tone']['tone']
        mockup = self.create_outfit_mockup(recommendation, skin_tone, gender)
        return mockup
    
    def create_style_guide_image(self, analysis, recommendations_list):
        """
        Create a style guide with multiple outfit options
        
        Args:
            analysis: Image analysis results
            recommendations_list: List of recommendations
            
        Returns:
            PIL Image with multiple outfit options
        """
        # Create canvas for grid
        cols = 2
        rows = (len(recommendations_list) + cols - 1) // cols
        mockup_size = 300
        
        total_width = mockup_size * cols + 40
        total_height = mockup_size * rows + 40
        
        canvas = Image.new('RGB', (total_width, total_height), color=(250, 250, 250))
        
        for idx, rec in enumerate(recommendations_list):
            row = idx // cols
            col = idx % cols
            
            mockup = self.create_outfit_mockup(rec, analysis['skin_tone']['tone'])
            # Resize mockup
            mockup = mockup.resize((mockup_size, mockup_size))
            
            x = col * mockup_size + 20
            y = row * mockup_size + 20
            
            canvas.paste(mockup, (x, y))
        
        return canvas
