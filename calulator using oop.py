class Calculator():
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

while True:
        my_cl = Calculator()
        print("SIMPLE CALCULATOR USING OOP CONCEPT")
        print("1 FOR ADDITION")
        print("2 FOR SUBTRACTION")
        print("3 FOR MULTIPLY")            
        print("4 FOR DIVISION")


        operator = input("Enter a number from 1,2,3,4:")

        a = int(input("Enter num1:"))
        b = int(input("Enter num2:"))            
        if operator == '1':
            result = my_cl.add(a, b)
            print(a, "+", b, "=", result)

        elif operator == '2':
             print(a, "-", b, "=", my_cl.subtract(a, b))

        elif operator == '3':
            print(a, "*", b, "=", my_cl.multiply(a, b))

        elif operator == '4':
             print(a, "/", b, "=", my_cl.divide(a, b))

        else:
             print("Invalid Input")




