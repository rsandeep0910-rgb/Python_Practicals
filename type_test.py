flight_no = "SA-0910"
base_fare = "5000.75"
tax_percentage = "5"
seat_numbers = "12A, 12B, 14C"
is_international = "true"

base_fare = float(base_fare)                                              #a
tax_percentage = float(tax_percentage)
final_fare = base_fare + (base_fare * tax_percentage / 100)
print("Final fare for one passenger:", final_fare)

seat_list = seat_numbers.split(", ")                                      #b
print("Seat numbers:", seat_list)

seat_list = set(seat_list)                                                #c
print("Unique seat numbers:", seat_list)

is_international = True if is_international.lower() == "true" else False  #d
print("Is the flight international", is_international) 

flight_summary = {                                                        #e
    "flight_no": flight_no,
    "final_fare": int(final_fare),
    "seat_numbers": tuple(seat_list),
}
print("Flight Summary:", flight_summary)
