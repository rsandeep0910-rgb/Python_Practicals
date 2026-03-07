class Product:
    def __init__(self,name,price,**kwargs):
        super().__init__(**kwargs)
        self.name = name 
        self.price= price
        print("We are into the Product Constructor")
        
    def display_basic(self):
        print(f"Product :{self.name} has the price as INR.{self.price}")
    
class Electronics(Product):
    def __init__(self,category,**kwargs):
        super().__init__(**kwargs)
        self.category = category
        print("We are into the Electronics Constructor")
        
    def display_category(self):
        print(f"Product :{self.name} has the price as INR.{self.price} with cateogry as {self.category}")
        
    
class Brand(Product):
    def __init__(self,brand,**kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        print("We are into the Brand Constructor")
        
    def display_brand(self):
        print(f"Product :{self.name} has the price as INR.{self.price} with brand as {self.brand}")
        
        
class MyProduct(Electronics,Brand):
    def __init__(self, name, price,category, brand, discount):
        super().__init__(name=name,price=price,category=category,brand=brand)
        self.discount= discount
        
    def all_details(self):
        print("we are into the all details method")
        self.display_category()
        self.display_brand()
        #self.display_basic()
        
mypro = MyProduct("Laptop", 45000, "Electronics", "DELL", 3000)
mypro.all_details()