def power(a, n):
    return a**n

def main():
    a = int(input("Enter the number: "))
    n = int(input("Enter the exponent: "))

    result = power(a, n)
  
    print(f"Power of {a} is: ", result)

main()
