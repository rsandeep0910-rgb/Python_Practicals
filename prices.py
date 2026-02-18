# Global discount variable (in percentage)
discount = 10   # 10% discount

# Function to display product details and calculate discounted price
def show_product_details(prod_id, prod_name, price):
    global discount
    
    discounted_price = price - (price * discount / 100)
    
    print("Product ID:", prod_id)
    print("Product Name:", prod_name)
    print("Original Price:", price)
    print("Discount:", discount, "%")
    print("Price After Discount:", discounted_price)
    
    return discounted_price


# Function to calculate total price based on quantity
def total_price_after_discount(price, quantity):
    global discount
    
    discounted_price = price - (price * discount / 100)
    total = discounted_price * quantity
    
    return total


# Example usage
#dp = show_product_details(101, "Laptop", 50000)

total_bill = total_price_after_discount(50000, 3)
print("Total Price for quantity:", total_bill)