'''
WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fai
'''
subject_1 = float(input("enter marks of first subject"))
subject_2 = float(input("enter marks of second subject"))
subject_3 = float(input("enter marks of third subject"))
subject_4 = float(input("enter marks of fourth subject"))
total_marks = subject_1 + subject_2 + subject_3 + subject_4
print("total marks is {total_marks} ")
percentage = total_marks//4
if percentage>70:
    print("you have scored distinction")
elif percentage>60:
    print("you have scored first division")
elif percentage>40:
    print("you have scored just pass marks")
else:
   print("you have failed your test")
