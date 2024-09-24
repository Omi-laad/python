'''f= open("test.txt","w")
f.write("asdfgh\n")
f.writelines(["omi","laad"])
f.close()
f =open("test.txt")
print(f.read)
f.seek(0)
print(f.readlines())
f.seek(0)
print(f.readlines())
'''
'''
try:
    x= int(input("ENTER X:"))
    y=int(input("ENTER Y:"))
    print(x/y)
except ValueError:
    print("ENTER A VALID INTEGER")
except ZeroDivisionError:
    print("ERROR OCCURED:")
finally:
       print("BYE")
'''
''''
class NetworkError(RuntimeError):
      def _init_(self,args):
          self.args = args

try:
    raise NetworkError("bad Hostname")
except NetworkError as e:
    print("".join(e.args))
    #print(e.args)
'''
'''
oop
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
              
    def print_user(self):
        print(self.name,self.email)
              
u = User("omilaad","omi@mail.com")
u.print_user()
'''
'''
class User:
   def __init__(self,name,email):
        self.name = name
        self.email = email

   def __str__(self):
       return self.name +" "+ self.email
   def print_user(self):
       print(self.name,self.email)
              
u = User("omilaad","omi@mail.com")
#u.print_user()
print(u)
'''
class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b


    def area(self):

        return self.length * self.breadth
class Square(Rectangle):
    def __init__(self,l):
        super().__init__(l,l)
r = Rectangle(2,4)
s = Square(4)
print(r.area())
print(s.area())
        
