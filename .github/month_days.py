11) Write a function to accept a month and year as input, and return the number of days in that month as output. print the number of days in main.


def get_days(month, year):
    if month in [1,3,5,7,8,10,12]: 
        return 31
    elif month in [4,6,9,11]: 
        return 30
    elif month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    else: 
        return -1  
        
def main():
    
    month = int(input("Enter a month(1-12): "))
    year = int(input("Enter a year: "))
    
    if get_days == -1:
        print("Invalid month")
    else: 
        print(f"Number of days in month {month}, year {year} is {get_days(month, year)}")
        
main()
