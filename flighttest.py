class Flight:
    def __init__(self, flight_no, source, destination, base_fare):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.base_fare = base_fare

    def display_flight_details(self):
        print(f"flight number: {self.flight_no}, source: {self.source}, destination: {self.destination}")

    def calculate_fare(self, passenger_count, discounted_percentage):
        total_fare = self.base_fare * passenger_count
         
        if discounted_percentage > 0:
            total_fare = total_fare - (total_fare * discounted_percentage / 100)
        return total_fare
    
    def update_route(self, source=None, destination=None):
        if source:
            self.source = source
        if destination:
            self.destination = destination
        
flight2 = Flight("SA-0910", "Mysuru", "Bengaluru", 500000000)

fare1 = flight2.calculate_fare(2,2)
print(f"Total fare with 10% discount: {fare1}")

fare2 = flight2.calculate_fare(3,2)
print(f"Total fare with no discount: {fare2}") 

flight2.update_route(destination="Mysuru")
print(f"Updated route (only destination):", flight2.source, "to", flight2.destination)
flight2.update_route(source="Bengaluru", destination="Mysuru")
print(f"Updated route (both):", flight2.source, "to", flight2.destination)