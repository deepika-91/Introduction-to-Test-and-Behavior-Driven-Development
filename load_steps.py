# features/steps/load_steps.py

from behave import given
from app.models import Product

@given('I load fake product data')
def step_impl(context):
    context.product = Product.create(name="Laptop", category="Electronics", price=999.99, availability=True)
    context.another_product = Product.create(name="Tablet", category="Electronics", price=399.99, availability=False)
