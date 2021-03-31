#q1:range from user? and tell about how many odd numbers
# alma=['a','b', 'c','d', 'a','b', 'c','d']

range_num = input("Please enter the range for series: ")
a=1
b=1
i=0
list=[1,1]
while i<int(range_num):
    c=a+b
    print(c)
    list.append(c)
    b = a
    a=c
    i=i+1
k=0
count=0
while k<range_num:
    if list[k]%2!=0:
        count+=1
    print(k)

