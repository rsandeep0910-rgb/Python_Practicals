import json 

with open("products.json","r") as product_stream:
    products = json.load(product_stream)   # reads the charcters from the stream
    
for p in products:
    print(p["id"],p["name"],p["price"],p["stock"])
    
print(type[products])
print(type[products[1]])

#-----------------------------reading the data in form of bytes 

with open("products.json","rb") as prod:   # stream --> bytes
    raw_bytes = prod.read()                # storing the bytes into raw_bytes
    
products = json.loads(raw_bytes.decode("utf-8"))  # bytes to be decoded into string --> json object

for p in products:
    print(p["name"])