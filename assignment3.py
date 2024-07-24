func = (input("enter the operation which you want to perform : "))

n = int(input("enter number of rows : "))
m = int(input("enter number of columns : "))
a = []
for i in range(0,n):
    x = []
    for j  in range(0,m):
        x.append(int(input("enter a number : ")))
    a.append(x)

n1 = int(input("enter number of rows: "))
m1 = int(input("enter number of columns: "))
b = []
for i in range(0,n1):
    y = []
    for j  in range(0,m1):
        y.append(int(input("enter a number : ")))
    b.append(y)

result = [[0 for j in range(m)] for i in range(n)]
if(len(a) == len(b)):              #first operation (addition)
     for i in range(0,n):
        for j in range(0,m):
            result[i][j] = a[i][j] + b[i][j]
if(func == "addition"):             
    print(result)

res = [[0 for j in range(m)] for i in range(n)]
if(len(a) == len(b)):               # second operation (subtraction)
    for i in range(0,n): 
        for j in range(0,m):
            result[i][j] = a[i][j] - b[i][j]
if(func == "subtraction"):       
    print(result)

#multiplication
mul = [[0 for j in range(m)] for i in range(n)]        # third operation (multiplication)
d = len(a)      #row 
e = len(a[0])   #this will tell us the number of columns in a
f = len(b[0])   #this will tell us the number of columns in b

for i in range(d):
    for j in range(e):
        for k in range(f):
            mul[i][j] += a[i][k] * b[k][j]
if(func == "multiplication" and len(a[0]) == len(b)):
    print("multiplicaton of a and b is : ",mul)
else:
    print("multiplication is not possible !")

#diagonal sum 
diag1 = 0
diag2 = 0        
for i in range(n):
    for j in range(m):
        if(i == j):
            diag1 += a[i][j]
if(func == "diagonalsum"):
    print("sum of diagonal element of first : ",diag1)
for i in range(n):
    diag2 += a[i][n - i - 1]
if(func == "diagonalsum2"):
    print("sum of diagonal elements : ",diag2)


#uppertraingular matrix 
def is_upper_triangular(a):
    n = len(a) 
    for i in range(n):
        for j in range(m):  
            if(i > j):
                if a[i][j] != 0:
                    return False
    return True
if(func == "upper_traingular"):
    if is_upper_triangular(a):
        print("a is upper triangular.")
    else:
        print("a is not upper triangular.")


#saddle point      
rows_index = 0
col_ind = 0
def findSaddlePoint(a, n):
    for i in range(0, n):
        min_row = a[i][0]
        rows_index = i 
        col_ind = 0
        for j in range(1, n):
            if a[i][j] < min_row:
                min_row = a[i][j]
                col_ind = j
        is_saddle_point = True
        for k in range(0, n):
            if a[k][col_ind] > min_row:
                is_saddle_point = False
                break
        if is_saddle_point:
            print("Value of Saddle Point:", rows_index, col_ind)
            return True
    return False

n = len(a)
res2 = findSaddlePoint(a, n)

if res2:
    print(rows_index,col_ind)
else:
    print("No saddle point found")

