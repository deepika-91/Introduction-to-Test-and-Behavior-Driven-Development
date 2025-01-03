# features/steps/web_steps.py

from behave import when, then
from app.models import Product

@when('I create a product')
def step_impl(context):
    product_data = {
        'name': "New Laptop",
        'category': "Electronics",
        'price': 1000.00,
        'availability': True
    }
    context.product = Product.create(**product_data)

@when('I update the product')
def step_impl(context):
    context.product.update(name="Updated Laptop", price=1100.00)

@when('I delete the product')
def step_impl(context):
    context.product.delete()

@when('I list all products')
def step_impl(context):
    context.products = Product.list_all()

@when('I search products by name "{name}"')
def step_impl(context, name):
    context.search_results = Product.find_by_name(name)

@when('I search products by category "{category}"')
def step_impl(context, category):
    context.search_results = Product.find_by_category(category)

@when('I search products by availability "{availability}"')
def step_impl(context, availability):
    context.search_results = Product.find_by_availability(availability)

@then('the product should be saved')
def step_impl(context):
    assert context.product.name == "New Laptop"

@then('the product details should be updated')
def step_impl(context):
    assert context.product.name == "Updated Laptop"
    assert context.product.price == 1100.00

@then('the product should be deleted')
def step_impl(context):
    assert Product.find_by_name("New Laptop") is None

@then('I should see a list of products')
def step_impl(context):
    assert isinstance(context.products, list)

@then('I should see "{name}" in the result')
def step_impl(context, name):
    assert name in [product.name for product in context.search_results]
