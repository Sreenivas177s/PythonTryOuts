#  TASK1
######################################################################################
# 1.1
def subtract(a, b): return a - b


def myReduce(func, input_list):
    temp = input_list[0]
    for i in input_list[1:]:
        temp = func(temp, i)
    print(temp)


myReduce(subtract, [100, 9, 8, 7, 6, 4])
#####################################################################################
#1.2
def isMultipleOf7(a):
    if a%7 != 0:
        return False
    else:
        return True

def myFilter(condition , input):
    for i in input:
        if  condition(i):
            input.remove(i)
    return input


print(myFilter(isMultipleOf7 , [1,2,3,4,7,8,9,14]))
####################################################################################
#2.1
word = "ACADGLID"
output = [i for i in word]
print(output)

#2.2
word1 = "xyz"
output1 = [j*num for j in word1 for num in range(1,5)]
print(output1)

#2.3
output3 = [i*num for num in range(1,5) for i in word1]
print(output3)

#2.4
output4 = [[i+num] for i in range(2,5) for num in range(0,3)]
print(output4)

#2.5
output4 = [[i+num for num in range(0,4)] for i in range(2,6)]
print(output4)

#2.6
output5 = [(j,i) for i in range(1,4) for j in range(1,4)]
print(output5)
############################################################################################
#3
def  longestWord(l):
    max = l[0]
    for i in l:
        if len(i) > len(max):
            max = i
    print("the Largest Word is :",max)


l = input("enter the list of words:\t").split()
longestWord(l)
############################################################################################
#   TASK-2
############################################################################################
#1.1
class triangle_properties:
    def __init__(self):
        self.a = int(input("enter side a : "))
        self.b = int(input("enter side b : "))
        self.c = int(input("enter side c : "))

class areaoftriangle(triangle_properties):
    def __init__(self, *args):
        super(areaoftriangle, self).__init__(*args)

    def area_tri(self,a,b,c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    def __str__(self):
        return "The area of the triangle is %s"%(self.area_tri(self.a, self.b, self.c))


a = areaoftriangle()
print(a)
############################################################################################
# 1.2
def filter_longwords(words, num):
    a = []
    for i in words:
        if len(i) <= num:
            a.append(i)
    words = a
    return words


l = input("enter the list of words separated by spaces : ").split()
n = int(input("enter the threshold number : "))
print(filter_longwords(l, n))
###########################################################################################
#2.1
def custom_map(words):
    for i in range(0,len(words)):
        words.append(len(words[0]))
        words.pop(0)
    return words


l = input("enter the list of words with spaces : ").split()
print(custom_map(l))
###########################################################################################
#2.2
def vowel(c):
    if c.lower() in ["a","e","i","o","u"]:
        print("the character {} is a vowel".format(c))
    else:
        print("the character {} is a not vowel".format(c))