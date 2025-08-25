1) Write a function to calculate simple interest. Call it in main function with appropriate inputs and print the total amount the user will get after the tenure (principle + interest)

def simple_interest(principal, rate, time):
    interest = (principal * rate * time )/100
    return interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time: "))

    interest = simple_interest(principal, rate, time)
    total_amount = principal + interest

    print("Simple interest is: ", interest)
    print("The total amount is:", total_amount)

main()

