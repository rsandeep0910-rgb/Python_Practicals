# Global variable
global_message = "Python is awesome!" # Declared outside a function

def my_function():
    # Local variable with a different name
    local_message = "This is local to my_function."
    print(f"Inside the function (local): {local_message}") #
    print(f"Inside the function (global): {global_message}") # Can access global variable

# Call the function
my_function()

# Access global variable outside the function
print(f"Outside the function (global): {global_message}")

# Attempting to access the local variable outside the function will cause an error
# print(local_message) # This would raise a NameError
