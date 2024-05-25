# Lesson 2: Tuples
# 5. Advanced Tuple Techniques: Joining and Nesting in Python

def merge_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

combined_catalog = merge_catalogs(catalog1, catalog2)

for product, price in combined_catalog:
    print(f"Product: {product}, Price: ${price:.2f}")
