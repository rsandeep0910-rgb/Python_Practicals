class Room:
    length = 0
    breadth = 0

    def __init__(self,length,breadth): #constructor
        self.length = length
        self.breadth = breadth

    def calculate_area(self,name):        #method
        c = self.length * self.breadth
        print(f"area of the {name} is {c}")

study_room = Room(42.0,10.0) #object 1
study_room.calculate_area("study room")

living_room = Room(120, 180) #object 2
living_room.calculate_area("Living room")

   #Living_room = Room(80.0,50.0)  #object 2
   #Living_room.length = 80
   #Living_room.breadth = 50
   #Living_room.calculate_area()

