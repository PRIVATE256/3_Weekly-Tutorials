# Create a program that converts different data types and outputs the results. 
# 1. Convert an integer to a floating-point number. 
# 2. Convert a floating-point number to an integer. 
# 3. Convert an integer to a string. 
# 4. Convert a string containing a number to an integer. 
# 5. Convert an integer to a Boolean

print('''
Programs Available:
 [1] Convert an integer to a floating-point number.
 [2] Convert a floating-point number to an integer.
 [3] Convert an integer to a string.
 [4] Convert a string containing a number to an integer.
 [5] Convert an integer to a Boolean.
''')

program = input("Select program to be executed: ")

if program == "1":
    zahl = int(input("Enter an integer: "))
    print("Float Value is : ", float(zahl))
elif program == "2":
    kommazahl = float(input("Enter a floating-point number: "))
    print("Integer Value is :", int(kommazahl))
elif program == "3":
    text = input("Enter an integer: ")
    if text.isdigit() == True:
        zahl = int(text)
        result = str(zahl)
        print("String Value is: ", repr(result), " of type", type(result))
    else:
        print("Invalid Data Entered!")
elif program == "4":
    text = input("Enter a string containing an integer: ")
    if text.isdigit() == True:
        zahl = int(text)
        print("Interger Value is :", int(zahl))
    else:
        print("Invalid Data Entered!")
elif program == "5":
    number = int(input("Enter an integer: "))
    print("Boolean Value is :", bool(number))
else:
    print("Invalid selection.")