n= input("ENTER NAME:")
r=input("ENTER ROLL NO:")
x= int(input("ENTER A MARKS OUT OF 100:"))
if x>100:
    print("PLEASE ENTER CORRECT MARKS")
    x= int(input("ENTER A MARKS OUT OF 100:"))
    if  x<40:
        print("SORRY TO INFORM YOU ",n,"YOU HAVE FAILED THE EXAM")
        print("DONT WORRY PICK YOURSELF UP AND TRY HARDER ALL THE BEST") 
    elif x>80:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH A GRADE ""KEEP THE MOMENTUM GOING ")
    elif x>70:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH B GRADE")
         print("KEEP THE MOMENTUM GOING ")
    elif x>60:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH C GRADE")
         print("STILL CAN SCORE MORE ")
    elif x>50:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH D GRADE")
         print("STUDY HARD!! ")
    elif x>=40:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH E GRADE")
         print(" BETTER START STUDING HARD")
else:
    if  x<40:
        print("SORRY TO INFORM YOU ",n,"YOU HAVE FAILED THE EXAM")
        print("DONT WORRY PICK YOURSELF UP AND TRY HARDER ALL THE BEST") 
    elif x>80:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH A GRADE ""KEEP THE MOMENTUM GOING ")
    elif x>70:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH B GRADE")
         print("KEEP THE MOMENTUM GOING ")
    elif x>60:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH C GRADE")
         print("STILL CAN SCORE MORE ")
    elif x>50:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH D GRADE")
         print("STUDY HARD!! ")
    elif x>=40:
         print("CONGRAULATIONS ",n,"YOU HAVE PASSED WITH E GRADE")
         print(" BETTER START STUDING HARD")
    
