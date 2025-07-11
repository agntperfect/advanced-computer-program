# Q no. 14:
# Build a dictionary where keys are product names and values are their prices.
# Implement functions to:
# a. Add a new product
# b. Update price of an existing product
# c. Find products within a given price range

def add_product(products, name, price):
    if name in products:
        return False
    products[name] = price
    return True

def update_price(products, name, new_price):
    if name not in products:
        return False 
    products[name] = new_price
    return True

def find_products_in_range(products, low, high):
    return {name: price for name, price in products.items() if low <= price <= high}


products = {
    "Laptop": 1000,
    "Phone": 500,
    "Headphones": 100,
    "Keyboard": 70,
}

added = add_product(products, "Mouse", 40)
print("Product added:", added)

updated = update_price(products, "Phone", 550)
print("Price updated:", updated)

in_range = find_products_in_range(products, 50, 600)
print("Products in price range 50 to 600:", in_range)