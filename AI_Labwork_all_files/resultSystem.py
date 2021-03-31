import math
subject1 = input("Enter 1st subject name: ")
subject2 = input("Enter 2nd subject name: ")
subject3 = input("Enter 3rd subject name: ")
subject4 = input("Enter 4th subject name: ")
subject5 = input("Enter 5th subject name: ")

marks1 = int(input("Enter 1st subject marks: "))
marks2 = int(input("Enter 2nd subject marks: "))
marks3 = int(input("Enter 3rd subject marks: "))
marks4 = int(input("Enter 4th subject marks: "))
marks5 = int(input("Enter 5th subject marks: "))

if marks1 >= 50:
    print(subject1 + "passed")
else:
    print(subject1 + "failed")
if marks2 >= 50:
    print(subject2 + "passed")
else:
    print(subject2 + "failed")
if marks3 >= 50:
    print(subject3 + "passed")
else:
    print(subject3 + "failed")
if marks4 >= 50:
    print(subject4 + "passed")
else:
    print(subject4 + "failed")
if marks5 >= 50:
    print(subject5 + "passed")
else:
    print(subject5 + "failed")

average = (marks1+marks2+marks3+marks4+marks5)/5
int(average)
if average>=90:
    print("you have got 4.0")
elif average>=85 and average<=89:
    print("you have got 3.7")
elif average>=80 and average<=84:
    print("you have got 3.3")
elif average>=75 and average<=79:
    print("you have got 3.0")
elif average>=70 and average<=74:
    print("you have got 2.7")
elif average>=65 and average<=69:
    print("you have got 2.3")
elif average>=60 and average<=64:
    print("you have got 3.0")



