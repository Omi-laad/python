
while True:
        pi=3.14
    
        print("1. FOR Triangle:")
        print("2. FOR Circle:")
        print("3. FOR Rectangle:")            
        print("4. FOR Square:")
        print("5. EXIT:")

        operator = input("Enter a number from 1,2,3,4,5:")
           
        if operator == '1':
            
            base = float(input("Enter value for base of traingle:"))
            height = float(input("Enter value for height of triangle:")) 
            print(0.5*base*height, "=", "is the Area of Tirangle")

        elif operator == '2':
            
             r = float(input("Enter value for radius of circle:"))
             print(pi*r*r, "=", "is the Area of Circle")

        elif operator == '3':
            
            l = float(input("Enter value for length of Rectangle:"))
            b = float(input("Enter value for breadth of Rectangle::")) 
            print(l*b, "=","is the Area of Rectangle")

        elif operator == '4':
             
              s = float(input("Enter  value of side of the Square:")) 
              print(4*s, "=","is the Area of Square")

        elif operator == '5':  
            break  
        else:  
            print("Oops! Incorrect Choice.")  
      



