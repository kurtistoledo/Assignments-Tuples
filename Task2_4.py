# Lesson 2: Tuples
# 4. Mastering Tuple Packing and Unpacking in Python

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Eve", "Smartphones", 3),
    ("Charlie", "Tablet", 1),
    ("David", "Headphones", 5),
]

# Process each order and print the details
for customer, product, quantity in orders:
    print(f"Customer: {customer}, Product: {product}, Quantity: {quantity}")
