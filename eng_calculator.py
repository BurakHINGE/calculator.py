def calc(x,y,operator):
    
    if operator not in "+-**/":
        return "You can only use +, -, *, /, ** operators!"

    if operator == "+":
        return(str(x) + " " + operator + " " + str(y) + " = " + str(x + y))

    if operator == "-":
        return(str(x) + " " + operator + " " + str(y) + " = " + str(x - y))

    if operator == "*":
        return(str(x) + " " + operator + " " + str(y) + " = " + str(x * y))

    if operator == "/":
        return(str(x) + " " + operator + " " + str(y) + " = " + str(x / y))

    if operator == "**":
        return(str(x) + " " + operator + " " + str(y) + " = " + str(x ** y))


while True:

    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    operator = input("Choose the operation you want to perform: +, -, *, /, ** :")

    print(calc(x,y,operator))
