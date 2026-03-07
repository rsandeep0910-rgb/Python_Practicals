class flight:
    def __init__(self,flight_no, price, total_seats):  
        self.flight_no = flight_no
        self.price= price
        self.total_seats = total_seats
        print("flight details are initialized")

   #  print(f"flight number is {self.flight_no} with price as {self.price} and total seats are {self.total_seats}")
        
    
class domestic_flight(flight):
   def __init__(self, flight_no, price, total_seats):
        super().__init__(flight_no, price, total_seats)
     #   print("domestic flight details are initialized")

        def calculate_price(self):
            total_price = self.price * self.total_seats
        #    print(f"price of domestic flight is {total_price}")

class booking_flight(domestic_flight):
    def __init__(self, flight_no, price, total_seats, discount):
        super().__init__(flight_no, price, total_seats)
        self.discount = discount
     #   print("booking flight are initialized")

        def book_seats(self, seats_to_book):
            if seats_to_book <= self.total_seats:
                self.total_seats -= seats_to_book
                total_price = (self.price * seats_to_book) - self.descount
                print(f"booked {seats_to_book} seats with total price as {total_price}")
            else:
                print("no seats available to book")

 # Example usage
flight1 = booking_flight("AI-100", 5200, 120, 8000)
flight1.display_flight_details()
#flight1.book_seats()


