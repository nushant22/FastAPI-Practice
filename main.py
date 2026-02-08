from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return("Hello, World!")

products = [
    Product(id = 1, name = "Phone", description = "Budget Phones",price = 9999, quantity = 10),
    Product(id = 2, name= "Laptop", description = "Budget Laptop", price = 59999, quantity = 5)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product      
    return "product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range (len(products)):
       if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"  
       
    return "No products found"


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Products deleted"
        
    return "Products not found"
        
