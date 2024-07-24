n = int(input("enter number of total students : "))
roll = []
while (n!=0):
    roll.append(int(input("enter roll number of all students : ")))
    n-=1
c = int(input("enter number of students who play cricket : "))
cric = []
while (c!=0):
    cric.append(int(input("enter roll number of students who play cricket : ")))
    c-=1
b = int(input("enter number of students who play badminton  : "))
bad = []
while (b!=0):
    bad.append(int(input("enter roll number of students who play badminton : ")))
    b-=1
football = []
f = int(input("enter number of students who play football : "))
while (f!=0):
    football.append(int(input("enter roll number of students who play football : ")))
    f-=1

# 1st --> list of students who play both cricket and badminton
new = []
for i in cric:
    for j in bad:
        if i == j and i not in new:
            new.append(i)
            break
print("list of students who play both cricket and badminton : ",new)

#2nd --> list of students who play either cricket or badminton but not both
both = []
for i in cric:
    if i not in bad:
        both.append(i)
for i in bad:
    if i not in cric:
        both.append(i);
print("list of students who play either cricket or badminton but not both : ",both)

#3rd --> Number of students who play neither cricket nor badminton 
sum = 0
for i in roll:
    if i not in bad and i not in cric:
        sum += 1
print("number of students who play neither cricket nor badminton : ",sum)

#4th --> Number of students who play cricket and football but not badminton
sum2 = 0
for player in cric:
    if player in football and player not in bad:
        sum2 += 1
print("Number of students who play cricket and football but not badminton : ",sum2)


#5th --> Number of students who do not play any game
sum3 =0
for student in roll:
    if student not in cric and student not in bad and student not in football:
        sum3 += 1
        
#6th --> list of students who play at least one game
l = []
for i in cric:
    if i not in l:
        l.append(i)
for i in bad:
    if i not in l:
        l.append(i)
for i in football:
    if i not in l:
        l.append(i)
print("List of students who play at least one game:", l)

#7th --> list of students who play all three games 
alll = []
for i in cric:
    if i in bad and i in football:
        alll.append(i)
print("students who play all three games : ",alll)