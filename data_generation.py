import pandas as pd
import random
from faker import Faker


def generate_data(num_products=1000):
    fake = Faker()

    # Define categories with expanded product names and descriptions
    category_products = {
        'Electronics': {
            'products': [
                {
                    'name': 'Smartphone',
                    'description': 'A high-tech gadget with reliability'
                },
                {
                    'name': 'Laptop',
                    'description': 'Portable computer for all your needs'
                },
                {
                    'name': 'Headphones',
                    'description': 'Headphones with noise cancellation'
                },
                {
                    'name': 'Camera',
                    'description': 'Digital camera with high resolution'
                },
                {
                    'name': 'Smartwatch',
                    'description': 'Smartwatch with fitness tracking'
                },
                {
                    'name': 'Tablet',
                    'description': 'Compact tablet with high performance'
                },
                {
                    'name': 'Smart TV',
                    'description': 'High-definition smart television'
                }
            ]
        },
        'Home': {
            'products': [
                {
                    'name': 'Vacuum Cleaner',
                    'description': 'Efficient cleaning for your home'
                },
                {
                    'name': 'Sofa',
                    'description': 'Comfortable and stylish seating'
                },
                {
                    'name': 'Microwave',
                    'description': 'Compact microwave for quick meals'
                },
                {
                    'name': 'Refrigerator',
                    'description': 'Large capacity fridge with freezer'
                },
                {
                    'name': 'Lamp',
                    'description': 'Elegant lamp for ambient lighting'
                },
                {
                    'name': 'Dishwasher',
                    'description': 'Automatic dishwasher for easy cleaning'
                }
            ]
        },
        'Gadgets': {
            'products': [
                {
                    'name': 'Drone',
                    'description': 'Quadcopter with HD camera'},
                {
                    'name': 'VR Headset',
                    'description': 'Virtual reality headset for fun'},
                {
                    'name': 'Smart Home Hub',
                    'description': 'Central hub for all your smart devices'},
                {
                    'name': 'Portable Charger',
                    'description': 'High capacity portable charger'},
                {
                    'name': 'Bluetooth Speaker',
                    'description': 'Wireless speaker with great quality'},
                {
                    'name': 'Smart Light Bulb',
                    'description': 'Energy-efficient smart light bulb'
                }
            ]
        },
        'Clothing': {
            'products': [
                {
                    'name': 'T-shirt',
                    'description': 'Comfortable cotton t-shirt'
                },
                {
                    'name': 'Jeans',
                    'description': 'Stylish denim jeans'
                },
                {
                    'name': 'Jacket',
                    'description': 'Warm jacket for cold weather'
                },
                {
                    'name': 'Sneakers',
                    'description': 'Trendy sneakers with good grip'
                },
                {
                    'name': 'Hat',
                    'description': 'Cool hat for sunny days'
                },
                {
                    'name': 'Scarf',
                    'description': 'Cozy scarf for winter'
                }
            ]
        },
        'Books': {
            'products': [
                {
                    'name': 'Mystery Novel',
                    'description': 'A gripping mystery novel'
                },
                {
                    'name': 'Science Fiction',
                    'description': 'Futuristic science fiction story'
                },
                {
                    'name': 'Cookbook',
                    'description': 'Recipes from around the world'
                },
                {
                    'name': 'Biography',
                    'description': 'Inspirational biography of a famous person'
                },
                {
                    'name': 'Self-Help',
                    'description': 'Guide to personal development and success'
                },
                {
                    'name': 'Fantasy Novel',
                    'description': 'An epic fantasy adventure'
                }
            ]
        },
        'Toys': {
            'products': [
                {
                    'name': 'Action Figure',
                    'description': 'Detailed action figure from popular series'
                },
                {
                    'name': 'Doll',
                    'description': 'Beautiful doll with accessories'
                },
                {
                    'name': 'Board Game',
                    'description': 'Fun board game for family and friends'
                },
                {
                    'name': 'Puzzle',
                    'description': 'Challenging puzzle to solve'
                },
                {
                    'name': 'RC Car',
                    'description': 'Remote-controlled car with high speed'
                },
                {
                    'name': 'Building Blocks',
                    'description': 'Creative building blocks for kids'
                }
            ]
        }
    }

    # Initialize lists to store data
    names = []
    descriptions = []
    prices = []
    category_labels = []

    for _ in range(num_products):
        # Randomly select a category
        category = random.choice(list(category_products.keys()))

        # Randomly select a product name and desc for the chosen category
        product = random.choice(category_products[category]['products'])
        name = product['name']
        description = product['description']

        # Introduce slight variations in product descriptions
        description += f" {fake.catch_phrase()}."

        # Generate random price between 5 and 500
        price = round(random.uniform(5.00, 500.00), 2)

        # Append generated data to lists
        names.append(name)
        descriptions.append(description)
        prices.append(price)
        category_labels.append(category)

    # Create a DataFrame
    data = {
        'name': names,
        'description': descriptions,
        'price': prices,
        'category': category_labels
    }
    df = pd.DataFrame(data)

    return df
