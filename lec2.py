x=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
for i in range(len(x)):
    for j in range(len(x[0])):
        print(x[i][j],end=" ")
    print()  
 
'''
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[]
print(x)
print(y)
for i in range(len(x)):
    temp =[]
    for j in range (len(x[0])):
        temp.append(x[i][j]+y[i][j])
    
    z.append(temp)
print(z)
'''
