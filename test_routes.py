# tests/test_routes.py

import unittest
from app import create_app
from app.models import Product

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_product(self):
        response = self.client.post('/products', json={'name': 'Laptop', 'category': 'Electronics', 'price': 999.99, 'availability': True})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Laptop', response.json['name'])

    def test_update_product(self):
        response = self.client.put('/products/1', json={'name': 'Updated Laptop', 'price': 1099.99})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated Laptop')

    def test_delete_product(self):
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 204)

    def test_list_all_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_find_product_by_name(self):
        response = self.client.get('/products?name=Laptop')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Laptop', response.json[0]['name'])

    def test_find_product_by_category(self):
        response = self.client.get('/products?category=Electronics')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Electronics', response.json[0]['category'])

    def test_find_product_by_availability(self):
        response = self.client.get('/products?availability=True')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json[0]['availability'])

if __name__ == '__main__':
    unittest.main()
