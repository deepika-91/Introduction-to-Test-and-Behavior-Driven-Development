# factories.py

from faker import Faker
import random

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        return {
            'name': fake.word(),
            'category': random.choice(['Electronics', 'Clothing', 'Books', 'Furniture']),
            'price': round(random.uniform(5.0, 500.0), 2),
            'availability': random.choice([True, False]),
            'description': fake.text()
        }

# Example usage:
fake_product = ProductFactory.create_fake_product()
print(fake_product)
