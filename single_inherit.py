class product:
    name = "Sandeep"
    price = 1000
    brand = "Apple"
    warranty = 2
    count = 20

    def display(self):
        print(f"This is a product is {self.brand}")

    def cal_price(self):
        price = self.price * self.count
        print(f"price is ", price)

class electronics(product):
    type = "mobile"
    count = 10

    def displayalldetails(self):
        print(f"This is a product of type  {self.type} with count {self.count}")

mobile = electronics()
mobile.display()
mobile.cal_price()
mobile.displayalldetails()
