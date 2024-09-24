class Calculator:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
calc = Calculator()
print(calc.add(2,8,3)) 
print(calc.add(2, 3, 4)) 