def read_first_product():
    file = open("products_new.txt",'r')  # open the file in read mode
    
    line = file.readlines() 
    print(line)
    
    file.close()
    
read_first_product()

print("========= read the data line by line ====================")

def disp():
    file = open("products_new.txt",'r') 
    
    for line in file:
        print(line.strip())
        
    file.close()

disp()