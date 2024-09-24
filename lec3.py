'''nums=[]
for i in range(1,101):
    nums.append(i)
print(nums)

nums =[i*i for i in range(1,101)if i%2==0]#  for faster programming
print(nums)
'''
'''
tables={1:2,2:4,3:6}
tables={i:i* i for i in range(15)if i %2!=0}
print(tables)
for i in tables.keys():
    print(i,tables[i])
'''
'''
def greet(name):

    print("HELLO",name)
greet("omi")

'''
'''
def greet(name1,name2):
    print("HELLO",name1,name2)

greet("john","om//i")
'''
'''
def  get_user():
     email =input("Enter a email :")
     return email

email = get_user()
print(email)
'''
'''
x=20
def xinput():

    x=input("Enter x:")
    print(x)
xinput()
print(x)
'''
'''
def greet(name="world"):

    print("HELLO",name)
greet()
greet("ok")
greet("omi")
'''
'''
def get_name(*name):
    print(name)

get_name("john","paul","omi")
'''
'''
def get_name(*name):
    print("HELLO",",".join(name))

get_name("john","paul","omi")
'''
'''
def print_user(**user):
    print(user)
print_user(fname="laad",lname="omi")
'''
'''
def print_user(**user):
    print(user)
    print(user["lname"])
print_user(fname="laad",lname="omi")
'''
'''
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
'''
#lambda
add =lambda x,y:x+y
x = int(input())
y = int(input())
print(add(x,y))
