def file_pointer_demo():
    file = open("products_new.txt",'r')  # open the file in read mode
    
    print("current position",file.tell())
    
    file.seek(11)
    
    print("get the pointer", file.tell())
    
    lines = file.readlines()
    print(lines)
    
    file.close()
    
file_pointer_demo()