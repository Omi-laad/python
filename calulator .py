while True:
    
        print("SIMPLE CALCULATOR ")
        print("1. FOR ADDITION:")
        print("2. FOR SUBTRACTION:")
        print("3. FOR MULTIPLY:")            
        print("4. FOR DIVISION:")
        print("5. EXIT:")

        operator = input("Enter a number from 1,2,3,4,:")
           
        if operator == '1':
            
            a = int(input("Enter num1:"))
            b = int(input("Enter num2:")) 
            print(a + b, "=", "is the sum")

        elif operator == '2':
            
             a = int(input("Enter num1:"))
             b = int(input("Enter num2:")) 
             print(a - b, "=", "is the difference")

        elif operator == '3':
            
            a = int(input("Enter num1:"))
            b = int(input("Enter num2:")) 
            print(a * b, "=","is the multiplication")

        elif operator == '4':
             
              a = int(input("Enter num1:"))
              b = int(input("Enter num2:")) 
              print(a /  b, "=","is the quotient")

        elif operator == '5':  
            break  
        else:  
            print("Oops! Incorrect Choice.")  
      



