# test_app.py

from app import create_product

def test_create_product():
    product_data = {
        "name": "Test Product",
        "price": 10.99
    }
    product = create_product(**product_data)
    
    assert product.name == product_data["name"]
    assert product.price == product_data["price"]