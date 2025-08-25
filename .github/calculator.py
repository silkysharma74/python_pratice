9) Write a calculator program with 5 functions below to do the operations of addition, subtraction, multiplication, division for quotient and division for remainder.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
 
def quotient(a,b):
    if b==0: 
        return "Error"
    else: 
        return a/b

def remainder(a,b):
    if b==0: 
        return "Error"
    else: 
        return a%b 

def main():

   a=int(input("Enter first number: "))
   b=int(input("Enter second number: "))
   choice = input("Enter operation(+, -, *, /, %): ")

   if choice == '+': 
        print("Result:", add(a,b))
   elif choice == '-':
        print("Result:", sub(a,b))
   elif choice == '*':
        print("Result:", mul(a,b))
   elif choice == '/':
        print("Result:", quotient(a,b))
   elif choice == '%':
        print("Result:", remainder(a,b))
 
   else: 
        print("Invalid choice")

main()

