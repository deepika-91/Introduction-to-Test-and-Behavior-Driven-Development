# tests/test_models.py

import unittest
from app.models import Product

class TestProductModel(unittest.TestCase):
    
    def test_create_product(self):
        product = Product.create(name='Laptop', category='Electronics', price=999.99, availability=True)
        self.assertEqual(product.name, 'Laptop')

    def test_update_product(self):
        product = Product.create(name='Laptop', category='Electronics', price=999.99, availability=True)
        product.update(name='Updated Laptop', price=1099.99)
        self.assertEqual(product.name, 'Updated Laptop')
        self.assertEqual(product.price, 1099.99)

    def test_delete_product(self):
        product = Product.create(name='Laptop', category='Electronics', price=999.99, availability=True)
        product.delete()
        self.assertIsNone(Product.find_by_name('Laptop'))

    def test_list_all_products(self):
        products = Product.list_all()
        self.assertIsInstance(products, list)

    def test_find_product_by_name(self):
        product = Product.create(name='Laptop', category='Electronics', price=999.99, availability=True)
        found_product = Product.find_by_name('Laptop')
        self.assertEqual(found_product.name, 'Laptop')

    def test_find_product_by_category(self):
        product = Product.create(name='Laptop', category='Electronics', price=999.99, availability=True)
        found_product = Product.find_by_category('Electronics')
        self.assertIn(product, found_product)

    def test_find_product_by_availability(self):
        product = Product.create(name='Laptop', category='Electronics', price=999.99, availability=True)
        found_product = Product.find_by_availability(True)
        self.assertIn(product, found_product)

if __name__ == '__main__':
    unittest.main()
