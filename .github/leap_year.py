10) Write a function to accept a year as input and return 1 if the year is a leap year, otherwise 0.


def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return 1
    else:
        return 0

def main():
    year = int(input("Enter a year: "))
    result = leap_year(year) 
    if result == 1:
        print(year, "is a Leap year")
    else:
        print(year, "is NOT a Leap Year ")


main() 
