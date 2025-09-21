class Operation:
    
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        if operator not in "+-*/":
            print("Please select a valid operation (+, -, *, /, :): ")

        if operator == "+":
            return num1 + num2 
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator in ["/", ":"]:
            return num1 / num2 
        

while True:
    num1 = int(input("Enter your first number: "))
    operator = input("Choose your operation: ")
    num2 = int(input("Enter your second number: "))

    operation1 = Operation(num1, num2, operator)
    print("Result:", operation1.calculate())
