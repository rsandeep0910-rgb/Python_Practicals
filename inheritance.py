class Animal:
    # name = "efg"
    
    def eat(self):
        print(f"This method is eat of Animal class")
        
class Dog(Animal):
    
    def display(self):
        print(f"The {self.name} is an animal and inside display") 
        
    def eat(self):
        super().eat() # caling the parent class method eat
        print(f"This method is eat of Dog Class")
        
labrador = Dog()
labrador.name = "ABC"
labrador.eat()
labrador.display()