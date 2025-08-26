12) Write a function ,that can take two integers, swap their values and print their new values. return type should be void. function should print the values.

def swap_numbers(a,b):
    
    temp = a
    a = b
    b = temp
    print(f"After swapping: a is {a}, b is {b}")
    
def main():
    
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        print(f"Before swapping: a is {a}, b is {b}")
        swap_numbers(a,b)
        
main()        
    
