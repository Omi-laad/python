  
def addition(num1,num2):  
    sum =num1+num2  
    print("Sum of Addition is :", sum)  
  
def subtraction(num1, num2):  
    diff = num1-num2
    print("Difference of numbers is:", diff)  
  
def division(num1,num2):  
    div=num1/num2  
    print("Quotitent of Division is:", div)  
  
def multiplication(num1 ,num2):  
    prod = num1 * num2  
    print("Product of number is:",prod)  
  

  
# printing the starting line  
print("WELCOME TO A SIMPLE CALCULATOR PROGRAM")  
  
# creating options  
while True:  
        print("1. Addition")  
        print("2. Subtraction")  
        print("3. Multiplication")  
        print("4. Division")
        print("5. Exit")  
        choice3 = int(input("Enter the Choice:"))  
  
        if choice3 == 1:  
            num1 = int(input("Enter Number 1 for Addition:"))
            num2 = int(input("Enter Number 2 for Addition:"))  
            addition(num1,num2)
              
        elif choice3 == 2:  
            num1 = int(input("Enter Number 1 for Subtraction:"))  
            num2 = int(input("Enter Number 2 for Subtraction:"))  
            subtraction(num1,num2)  
              
        elif choice3 == 3:  
            num1 = int(input("Enter Number 1 for Multiplication:"))  
            num2 = int(input("Enter Number 2 for Multiplication:"))   
            multiplication(num1 ,num2)
  
        elif choice3 == 4:  
            num1 = int(input("Enter Number 1 for Division:"))  
            num2 = int(input("Enter Number 2 for Division:"))   
            division(num1 ,num2)

        
  
        elif choice3 == 5:  
            break  
        else:  
            print("Oops! Incorrect Choice.")  
      

      
     
