2) Write a function that takes two numbers, a and n as input arguments and returns the value of a to the power of n.

def power(a, n):
    return a**n

def main():
    a = int(input("Enter the number: "))
    n = int(input("Enter the exponent: "))

    result = power(a, n)
  
    print(f"Power of {a} is: ", result)

main()
