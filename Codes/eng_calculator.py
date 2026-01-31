class Operation:
    
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):

        valid_ops = ["+", "-", "*", "/", ":", "**"]

        if self.operator not in valid_ops:
            return "Please select a valid operator (+, -, *, /, :, **):"

        if self.operator == "+":
            return self.num1 + self.num2
        
        elif self.operator == "-":
            return self.num1 - self.num2
        
        elif self.operator == "*":
            return self.num1 * self.num2
        
        elif self.operator in ["/", ":"]:
            return self.num1 / self.num2

        elif self.operator == "**":
            return self.num1 ** self.num2


while True:
    num1 = int(input("Enter your first number: "))
    operator = input("Choose an operator: ")
    num2 = int(input("Enter your second number: "))

    operation = Operation(num1, num2, operator)
    print("Result:", operation.calculate())
