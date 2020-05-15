# Task-1
########################################################################################################################
#1.
def exception_handle(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot be divided by zero")
a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))
exception_handle(a,b)
########################################################################################################################
#2.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for k in objects:
            print(i + j + k)
########################################################################################################################
# Task - 2
#1
ip = input("enter input Numbers separated by spaces : ").split()
matrix = []
for i in ip:
    temp = []
    for j in range(len(ip)):
        temp.append(int(i)**j)
    matrix.append(temp)
for i in matrix:
    print(i)