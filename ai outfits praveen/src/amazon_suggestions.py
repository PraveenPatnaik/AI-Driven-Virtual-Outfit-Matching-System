"""
Amazon Product Suggestions Module
Generates Amazon product links based on outfit recommendations and gender
"""

AMAZON_SUGGESTIONS = {
    'Male': {
        'formal': [
            {
                'name': 'Premium Formal Blazer',
                'link': 'https://www.amazon.com/s?k=mens+formal+blazer',
                'colors': ['black', 'navy', 'gray']
            },
            {
                'name': 'Oxford Button-Down Shirt',
                'link': 'https://www.amazon.com/s?k=mens+oxford+button+down+shirt',
                'colors': ['white', 'light blue', 'gray']
            },
            {
                'name': 'Formal Dress Pants',
                'link': 'https://www.amazon.com/s?k=mens+formal+dress+pants',
                'colors': ['black', 'navy', 'gray']
            },
            {
                'name': 'Leather Dress Shoes',
                'link': 'https://www.amazon.com/s?k=mens+leather+dress+shoes',
                'colors': ['black', 'brown']
            }
        ],
        'traditional': [
            {
                'name': 'Traditional Kurta',
                'link': 'https://www.amazon.com/s?k=mens+traditional+kurta',
                'colors': ['cream', 'beige', 'gold', 'navy']
            },
            {
                'name': 'Embroidered Nehru Jacket',
                'link': 'https://www.amazon.com/s?k=mens+nehru+jacket',
                'colors': ['maroon', 'navy', 'black', 'gold']
            },
            {
                'name': 'Ethnic Dhoti Pants',
                'link': 'https://www.amazon.com/s?k=mens+dhoti+pants',
                'colors': ['cream', 'gold', 'white', 'navy']
            },
            {
                'name': 'Traditional Mojari Shoes',
                'link': 'https://www.amazon.com/s?k=traditional+mojari+shoes',
                'colors': ['gold', 'brown', 'navy', 'maroon']
            }
        ],
        'casual': [
            {
                'name': 'Casual Cotton T-Shirt',
                'link': 'https://www.amazon.com/s?k=mens+casual+cotton+tshirt',
                'colors': ['navy', 'black', 'gray', 'white']
            },
            {
                'name': 'Comfortable Jeans',
                'link': 'https://www.amazon.com/s?k=mens+jeans',
                'colors': ['light blue', 'dark blue', 'black']
            },
            {
                'name': 'Casual Sneakers',
                'link': 'https://www.amazon.com/s?k=mens+casual+sneakers',
                'colors': ['white', 'black', 'gray']
            },
            {
                'name': 'Cotton Hoodie',
                'link': 'https://www.amazon.com/s?k=mens+hoodie',
                'colors': ['black', 'gray', 'navy']
            }
        ],
        'western': [
            {
                'name': 'Denim Jacket',
                'link': 'https://www.amazon.com/s?k=mens+denim+jacket',
                'colors': ['blue', 'black']
            },
            {
                'name': 'Boots',
                'link': 'https://www.amazon.com/s?k=mens+boots',
                'colors': ['brown', 'black']
            },
            {
                'name': 'Flannel Shirt',
                'link': 'https://www.amazon.com/s?k=mens+flannel+shirt',
                'colors': ['red', 'blue', 'black', 'green']
            },
            {
                'name': 'Cowboy Hat',
                'link': 'https://www.amazon.com/s?k=cowboy+hat',
                'colors': ['brown', 'black']
            }
        ]
    },
    'Female': {
        'formal': [
            {
                'name': 'Elegant Blazer',
                'link': 'https://www.amazon.com/s?k=womens+elegant+blazer',
                'colors': ['black', 'navy', 'burgundy']
            },
            {
                'name': 'Formal Dress',
                'link': 'https://www.amazon.com/s?k=womens+formal+dress',
                'colors': ['black', 'navy', 'burgundy', 'gold']
            },
            {
                'name': 'Formal Heels',
                'link': 'https://www.amazon.com/s?k=womens+formal+heels',
                'colors': ['black', 'nude', 'gold', 'silver']
            },
            {
                'name': 'Formal Clutch',
                'link': 'https://www.amazon.com/s?k=womens+formal+clutch',
                'colors': ['black', 'gold', 'silver']
            }
        ],
        'traditional': [
            {
                'name': 'Elegant Saree',
                'link': 'https://www.amazon.com/s?k=womens+saree',
                'colors': ['maroon', 'navy', 'gold', 'pink']
            },
            {
                'name': 'Embroidered Blouse',
                'link': 'https://www.amazon.com/s?k=saree+blouse+embroidered',
                'colors': ['gold', 'maroon', 'cream', 'navy']
            },
            {
                'name': 'Traditional Bangles Set',
                'link': 'https://www.amazon.com/s?k=traditional+bangles+set',
                'colors': ['gold', 'maroon', 'green', 'multicolor']
            },
            {
                'name': 'Embellished Heels',
                'link': 'https://www.amazon.com/s?k=embellished+heels+womens',
                'colors': ['gold', 'maroon', 'navy', 'red']
            }
        ],
        'casual': [
            {
                'name': 'Casual Blouse',
                'link': 'https://www.amazon.com/s?k=womens+casual+blouse',
                'colors': ['white', 'navy', 'pink', 'gray']
            },
            {
                'name': 'Comfortable Leggings',
                'link': 'https://www.amazon.com/s?k=womens+leggings',
                'colors': ['black', 'navy', 'gray']
            },
            {
                'name': 'Casual Sneakers',
                'link': 'https://www.amazon.com/s?k=womens+casual+sneakers',
                'colors': ['white', 'black', 'pink', 'gray']
            },
            {
                'name': 'Crossbody Bag',
                'link': 'https://www.amazon.com/s?k=womens+crossbody+bag',
                'colors': ['black', 'brown', 'navy']
            }
        ],
        'western': [
            {
                'name': 'Denim Shirt',
                'link': 'https://www.amazon.com/s?k=womens+denim+shirt',
                'colors': ['light blue', 'dark blue', 'black']
            },
            {
                'name': 'Cowboy Boots',
                'link': 'https://www.amazon.com/s?k=womens+cowboy+boots',
                'colors': ['brown', 'black', 'tan']
            },
            {
                'name': 'Western Belt',
                'link': 'https://www.amazon.com/s?k=western+belt',
                'colors': ['brown', 'black', 'tan']
            },
            {
                'name': 'Wide-Brim Hat',
                'link': 'https://www.amazon.com/s?k=womens+wide+brim+hat',
                'colors': ['brown', 'black', 'tan']
            }
        ]
    }
}

class AmazonSuggestions:
    """Generate Amazon product suggestions based on analysis and recommendations"""
    
    @staticmethod
    def get_suggestions(gender, outfit_type, colors=None):
        """
        Get Amazon product suggestions
        
        Args:
            gender: 'Male' or 'Female'
            outfit_type: 'formal', 'casual', or 'western'
            colors: Optional list of preferred colors
            
        Returns:
            List of product suggestions with Amazon links
        """
        try:
            if gender not in AMAZON_SUGGESTIONS:
                gender = 'Female'  # Default
            
            if outfit_type not in AMAZON_SUGGESTIONS[gender]:
                outfit_type = 'casual'  # Default
            
            suggestions = AMAZON_SUGGESTIONS[gender][outfit_type]
            
            return {
                'gender': gender,
                'outfit_type': outfit_type,
                'products': suggestions,
                'message': f'Amazon suggestions for {gender} - {outfit_type.capitalize()} style'
            }
        
        except Exception as e:
            print(f"Error generating Amazon suggestions: {e}")
            return {
                'gender': gender,
                'outfit_type': outfit_type,
                'products': [],
                'message': f'Could not generate suggestions: {str(e)}'
            }
