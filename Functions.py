'''
def smallestNum():
    a = int(input('Enter number 1: '))
    b = int(input('Enter number 2: '))
    if a<b:
        print('Smallest number is: ',a)
        print('The greater number is: ',b)
    if a>b:
        print('Smallest number is: ',b)
        print('The greater number is: ',a)   
    else:
        print('The numbers are equal')
        
smallestNum()

def stringComp():
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    len_s1 = len(str1)
    len_s2 = len(str2)
    if len_s1>len_s2:
        print('String 1 is longer than string 2')
        print(str1+' is longer than '+str2)
        l = len_s1-len_s2
        print('Longer by '+str(l)+' characters')
    elif len_s2>len_s1:
        print('String 2 is longer that string 1')
        print(str2+' is longer than '+str1)
        l = len_s2-len_s1
        print('Longer by '+str(l)+' characters')
    else:
        print('Strings are equal')
        
stringComp()

def addition(a, b):
    print('Sum of A and B is ', a+b)
 
a = 12
b = 23
addition(a, b)
    
p = 65
y = 87
addition(p, y)

addition(10, 57)


from __future__ import division


def smallestNum():
    a = int(input('Enter number 1: '))
    b = int(input('Enter number 2: '))
    if a<b:
        print('The smaller number is: ',a)
        print('The bigger number is: ',b)
    
    if a>b:
        print('The smaller number is: ',b)
        print('The greater number is: ',a)
    else:
        print('The numbers are equal')

smallestNum()

def stringComp():
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    len_s1 = len(str1)
    len_s2 = len(str2)
    if len_s1>len_s2:
        print("String 1 is longer than string 2")
        print(str1+' is longer than '+str2)
        l = len_s1-len_s2
        print("Longer by "+str(1)+' characters')
    elif len_s2>len_s1:
        print('String 2 is longer than string 1')
        print(str2+' is longer than '+str1)
        l = len_s2-len_s1
        print('Longer by '+str(1)+' characters')
    else:
        print(' Both the strings are equal')

stringComp()



from __future__ import division


yoga = input('Are you trying your best in yoga class?: ')
if yoga == 'Yes':
    print("That's great! Keep trying, it will work out in end. Someone once said that change is messy in the beggining and amazing at the end.")
if yoga == 'No':
    print("You have to try because you don't know what fun it might be if you never try.")

highland = input('Are you enjoying my Highland Elementary and having fun with your friends?: ')
if highland == 'Yes':
    print("That's great, happy you are having fun!")
if highland == "No":
    print("Sorry, you are having a bad time! What is wrong?")
'''
classes = input('Are you enjoying your Math and English classes?: ')
if classes = 'Yes': ("That is amazing, keep up the great work!")

