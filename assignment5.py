
#liner search 

arr = []
n = int(input("enter number of students : "))
a = n
x = int(input("enter the roll number which you want : "))
while(n!=0):
    m = int(input("enter roll number of student : "))
    arr.append(m)
    n-=1
y = 0
ans = 0
for i in arr:
    ans+=1
    if i == x:
        y = 1
        break
if(y > 0):
    print("yes the student is present in the class")
else:
    print("student is enjoying his life ! ")
print("number of times the pointer has moved : ",ans)


# Binary search

arr.sort()
cnt = 0
i = 0
j = a - 1
yy = 0
while(i <= j):
    mid = (int)((i + j)/2)
    if arr[mid] == x:
        y = 1
        cnt+=1
        print("student is present in the class")
        break
    elif(arr[mid] < x):
        cnt += 1
        i = mid + 1
    else:
        cnt += 1
        j = mid - 1
if(y == 0):
    print("the student is enjoying his life !")
print("the number of times the pointer has moved : ",cnt)  

# lo + (high - lo)/2  another way of writing mid 

# sentinel search 

arr.append(x)
i = 0
while arr[i] != x:
    i+=1
if(i < a):
    print(i)
else:
    print(-1)
