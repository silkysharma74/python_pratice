Write a function to determine if a character is alphanumeric or not and print the appropriate output in main function. (return 1 if it is alphanumeric, 0 if it is not alpha numeric).

def fun_alpha_num(c):
    
    if c.isalnum():
        return 1
    else:
        return 0

def main():
    try:
        ch = input("Enter a single character: ")
        
        if len(ch) != 1:
            print("Please enter only ONE character.")
            return
        
        result = fun_alpha_num(ch)

        if result == 1:
            print(ch, "is Alphanumeric.")
        else:
            print(ch, "is NOT Alphanumeric.")

    except:
        print("Error occurred!")


main()
