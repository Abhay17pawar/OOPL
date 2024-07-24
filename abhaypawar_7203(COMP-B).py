n = int(input("Enter number of students: "))
a =n
sum_marks = 0
marks_list = []
p = 0 
f = 0
dict = {}
absent = 0
while n > 0:
    m = int(input("Enter marks of student: "))
    # to calculate marks with highest frequency 
    if m not in dict : 
        dict[m] = 0
    dict[m]+=1
    if(m < 0):       #absent 
       absent+=1
    else:
        marks_list.append(m)
        sum_marks+=m
        if(m >= 75):
            p+=1
        elif(m < 75):
            f+=1
    n -= 1

a = a-absent
average_marks = sum_marks / a  #average  marks
print("Average marks:", average_marks)
marks_list.sort()

print("Minimum marks:", marks_list[0]) # least marks 
print("Maximum marks:", marks_list[-1]) # highest marks 

print("number of present students",a) #number of present students 

percentage_passed = (p / a) * 100
percentage_failed = (f / a) * 100

print("Percentage of students who passed:", percentage_passed) #percentage of passed students
print("Percentage of students who failed:", percentage_failed) #percentage of failed students

# highest frequency of marks obtained by students
freq_marks = max(dict, key=dict.get)
print("highest frequency ",freq_marks)

