'''x=8
if x%2==0:
    print("x is even ")

else:
    print("x is odd")
    
x=8
if x==0:
    print(" x is zero")
elif x>0:
    print("x is positive")
else :
    print("x is negative")
'''
'''word = input("Enter a word:")
for  c in word:
    print(c , end="")
'''
'''for i in range(,10):
    print(i)
'''
'''for i in range(101):
     if i%2==0:
         print("EVEN NUMBER ARE :",i)
     else:
         print("odd number are ",i)
'''
'''x=0
while x<10:
    print(x)
    x+=1
'''
'''
x=0
while x<101:
     x+=1
     if x%2!=0:
        print(x)
 '''
'''x=0
while x<101:
    x+=1
   #find prime number solution 
    if x/2==0:
        print("Prime number are",x)
    if x:
        print("Composite numbers are",x)
'''
'''
my_list=['apple','oranges','mangoes']
my_list.insert(-2,"abcd")
#my_list.append("abed")
#my_list.remove('apple')
my_list.pop(1)
'''
'''
print(my_list)
x=[1,2,3]
y=[4,5,6]
x.extend(y)
print(x)
'''
'''
x=[1,2,3]
x.clear()
print(x)
'''
'''
x=["apples","mangoes","watermelon"]
print(x.index("mangoes"))
'''
'''
x=["apples","mangoes","watermelon"]
print(x.count("mangoes"))      
'''
'''
x=["apples","mangoes","watermelon"]
print(x.reverse)
'''
'''
x=("apples","mangoes","watermelon")
print(x[0])
#tuple
'''
'''
x={"oranges","apples","mangoes","mangoes"}
x.remove("oranges")
x.add("avacodes")
print(x)
'''
'''
x=[1,2,3,1,5,3]
y=set(x)
print(y)
if len(x)==len(y):
    print("no duplicates")
else:
    print("duplicates")
'''
'''
user={
   'name':'omi',
   'email':'omi@mail.com',
    }
print(user.keys())
print(user.values())
print(user.items())
for i in user.keys():
    print(i,user[i])
'''
'''
user={ }
fname= input("enter first name")
lname= input("enter last name")
user['first_name']=fname
user['last_name']=lname
print(user)
'''
