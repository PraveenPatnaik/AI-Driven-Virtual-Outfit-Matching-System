"""
Constants and configuration for AI Outfit Recommendation System
"""

# File upload constraints
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Outfit types available
OUTFIT_TYPES = {
    'traditional': 'Traditional',
    'western': 'Western',
    'casual': 'Casual'
}

# Skin tone categories
SKIN_TONES = {
    'light': 'Light',
    'medium': 'Medium',
    'dark': 'Dark'
}

# Face shapes
FACE_SHAPES = {
    'round': 'Round',
    'oval': 'Oval',
    'square': 'Square',
    'heart': 'Heart',
    'oblong': 'Oblong'
}

# Outfit recommendations based on outfit type and skin tone
OUTFIT_RECOMMENDATIONS = {
    'traditional': {
        'light': {
            'colors': ['Pastel Pink', 'Cream', 'Light Gold', 'Soft Blue'],
            'styles': ['Elegant Saree', 'Embroidered Kurti', 'Lehenga Choli'],
            'accessories': ['Gold Jewelry', 'Bindi', 'Traditional Bangles']
        },
        'medium': {
            'colors': ['Warm Gold', 'Deep Red', 'Rich Green', 'Maroon'],
            'styles': ['Silk Saree', 'Designer Kurti', 'Anarkali Suit'],
            'accessories': ['Gold/Silver Jewelry', 'Bindi', 'Jhumka Earrings']
        },
        'dark': {
            'colors': ['Deep Gold', 'Emerald Green', 'Royal Blue', 'Wine Red'],
            'styles': ['Rich Saree', 'Embellished Kurti', 'Heavy Lehenga'],
            'accessories': ['Gold Jewelry', 'Bindi', 'Statement Necklace']
        }
    },
    'western': {
        'light': {
            'colors': ['White', 'Light Grey', 'Beige', 'Pastel Blue'],
            'styles': ['Denim Jacket', 'White T-shirt', 'Light Dress'],
            'accessories': ['Silver Jewelry', 'Sneakers', 'Minimal Necklace']
        },
        'medium': {
            'colors': ['Navy Blue', 'Khaki', 'Burnt Orange', 'Charcoal'],
            'styles': ['Fitted Jeans', 'Stylish Blazer', 'Casual Dress'],
            'accessories': ['Silver/Gold Jewelry', 'Loafers', 'Watch']
        },
        'dark': {
            'colors': ['Black', 'Deep Navy', 'Burgundy', 'Dark Green'],
            'styles': ['Black Jeans', 'Leather Jacket', 'Formal Dress'],
            'accessories': ['Gold Jewelry', 'Heels', 'Sunglasses']
        }
    },
    'casual': {
        'light': {
            'colors': ['Pastel', 'White', 'Light Blue', 'Cream'],
            'styles': ['T-shirt', 'Shorts', 'Casual Shirt'],
            'accessories': ['Simple Necklace', 'Sneakers', 'Cap']
        },
        'medium': {
            'colors': ['Solid Tones', 'Earth Tones', 'Muted Colors'],
            'styles': ['Casual Tee', 'Comfortable Pants', 'Hoodie'],
            'accessories': ['Backpack', 'Sneakers', 'Simple Bracelet']
        },
        'dark': {
            'colors': ['Bold Colors', 'Dark Tones', 'Rich Colors'],
            'styles': ['Graphic Tee', 'Trendy Pants', 'Casual Jacket'],
            'accessories': ['Stylish Shoes', 'Cool Backpack', 'Watch']
        }
    }
}

# Rating descriptions
RATING_DESCRIPTIONS = {
    (1, 3): "Room for improvement - Consider style adjustments",
    (4, 5): "Good look - Nice effort with your outfit choice",
    (6, 7): "Very good - Well-coordinated and stylish",
    (8, 9): "Excellent - Confident and impressive appearance",
    (10, 10): "Perfect - Absolutely stunning look!"
}

# Compliment texts for different ratings
COMPLIMENTS = {
    (1, 3): [
        "Let's explore more styles together",
        "Great starting point for your outfit journey",
        "Room for a bit of polish"
    ],
    (4, 5): [
        "Nice coordination!",
        "Good style sense showing",
        "Well-put-together appearance"
    ],
    (6, 7): [
        "Very stylish choice!",
        "Excellent color coordination",
        "Confident and well-dressed"
    ],
    (8, 9): [
        "Absolutely stunning!",
        "Impeccable taste in fashion",
        "Radiant and fashionable"
    ],
    (10, 10): [
        "Perfection achieved!",
        "You're a style icon!",
        "Absolutely breathtaking!"
    ]
}
