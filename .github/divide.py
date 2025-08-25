4) Write a function that takes two numbers a and b, and returns the quotient after dividing a with b.


def divide_num(a, b):
    if b==0: 
        return "Error"
    else: 
        return a/b

def main():
    a = 20
    b = 5
  
    result = divide_num(a, b)
  
    print("Quotient is:", result) 

main()
