
3) Write a function that takes two numbers a and b as input arguments and returns their product as return value , without using * operator.
    
def product(a, b):
    return a * b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = product(a, b)
  
    print("Product is:", result) 

main()
