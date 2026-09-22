# Create a program that will calculate the factorial 

# x! = 1 * 2 * 3 * ... * (x -1) * (x)

value = int(input("Enter value to be factorialise : "))

if value >= 0:
    # 0! = 1 so this solves for that as well
    result = 1
    temp = value

    while temp != 0:
        result *= temp
        temp -= 1

    print(value, "! = ", result)

else:
    print("Negative number entered => factorial of a negative integer is undefined in standard mathematics")

