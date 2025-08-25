6) Write a function that takes an integer number as input and prints its multiplication table.return type is  void.
def print_table(num):
    for i in range(1,11):
        print(num, "x", i, "=", num * i)

def main():
        n = int(input("Enter a integer: "))
        print_table(n)
    

main()

