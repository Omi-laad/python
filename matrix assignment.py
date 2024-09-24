print("DISPLAY MATRIX 1:")
c=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j],end=" ")
    print()  
print("DISPLAY MATRIX 2:")
d=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j],end=" ")
    print()  

  
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[]
print("ADDITION OF 2 MATRIX:")      
for i in range(len(x)):
    temp =[]
    for j in range (len(x[0])):
        temp.append(x[i][j]+y[i][j])
    
    z.append(temp)
for i in range(len(z)):
    for j in range(len(z[0])):
        print(z[i][j],end=" ")
    print()  
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[]
print("SUBTRACTION OF 2 MATRIX:")      
for i in range(len(x)):
    temp =[]
    for j in range (len(x[0])):
        temp.append(x[i][j]-y[i][j])
    
    z.append(temp)
for i in range(len(z)):
    for j in range(len(z[0])):
        print(z[i][j],end=" ")
    print()  
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[]
print("MULTIPLICATION OF 2 MATRIX:")      
for i in range(len(x)):
    temp =[]
    for j in range (len(x[0])):
        temp.append(x[i][j]*y[i][j])
    
    z.append(temp)
for i in range(len(z)):
    for j in range(len(z[0])):
        print(z[i][j],end=" ")
    print()  
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
z=[]
print("DIVISION OF 2 MATRIX:")      
for i in range(len(x)):
    temp =[]
    for j in range (len(x[0])):
        temp.append(x[i][j]/y[i][j])
    
    z.append(temp)
for i in range(len(z)):
    for j in range(len(z[0])):
        print(z[i][j],end=" ")
    print()  
m = [[1,2,3],[4,5,6],[7,8,9]]
print("TRANSPOSE OF MATRIX 1")
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)
n=[[1,2,3],[4,5,6],[7,8,9]]
print("TRANSPOSE OF MATRIX 2")
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)
