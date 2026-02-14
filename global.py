message = "outer-variable"

# outside function 
def outer():
    message = 'local'
    print("inner:", message)
    
    # nested function  
    def inner():

         #global message
        # declare nonlocal variable
        nonlocal message

        #message = 'nonlocal'
        print("inner $$$$:", message)

    inner()
    print("outer:", message)

outer()
print("outside the outer_func", message)