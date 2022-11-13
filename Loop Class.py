#Strings Test Practice

'''
name = input('What is your name: ')
color =input('What is your favorite color: ')
print(name,"'s favorite color is", color)

#Loop Practice

for i in range(13):
    print(i+1, 'Lohith Thimmichetty')

for i in range(10):
    print(i+1, 'Lake Stevens')
    
for i in range(1):
    print(i+1, 'North Lake Middle School')

for i in range(8):
    print(i+1, 'Lohith Thimmichetty')
    print(i+1, 'Lake Stevens')
    print(i+1, 'North Lake Middle School')

for i in range(0,100,8):
     print(i,'North Lake Middle School')

for i in range(0,43,2):
    print(i+1, 'Lohith Thimmichetty')
    print(i+1, 'Lake Stevens')
    print(i+1, 'North Lake Middle School')
    print(i+1, 'Stella Schola Middle School')
    
s = 'Lohith Thimmichetty'
for i in s:
    print(i)
    
i = 1
while i<101:
    print(i, 'LOHITH T')
    i=i+1
    
for i in range(1,101):
    print(i, 'Lohith')

i = 1
while i<=10:
    print(i)
    i = i+1

i = 6
while i<=66:
    print(i)
    i = i+1
    
i = 9
while i<=99:
    print(i)
    i = i+1
    
i = 25
j = 1
while i<=250:
    print('25 x' , j , '=' , i)
    i = i+25
    j = j+1


for i in range (1,10):
    print('10x',i,'=',i*10)

l = [23,76,45,97,45,67]
count = 0
for elem in l:
    if elem == 45:
        count = count + 1
print('Count of 45 in the list',count)

i ='Lohith'
count = 0
for elem in i:
    if elem == 'h':
        count = count + 1
print('Count of h in the list is',count)

for i in range (1, 56):
    print('7x',i,'=',i*7)

for i in range (1, 12):
    print('8 x',i,'=',i*8)
    
for i in range (1, 5):
    print('1346 x',i,'=',i*1346)
    
for i in range(0,12,2):
    print(i+1, 'Lohith Thimmichetty')
    print(i+1, 'City of Lake Stevens')
    print(i+1, 'North Lake Middle School')
    print(i+1, 'Stella Schola Middle School')

s = 'Lohith Thimmichetty'
for i in s:
    print(i)
    



l = [12, 123, 1234, 12345, 123456]
for i in l:
    print(i, end='&$!@#%^* ')
    
num = [12345, 123, 123454321, 123432, 123, 8908908, 123456765432123454321, 123432123, 1234321, 12321]
for i in range(len(num)):
    print(i, num[i])
    
num = [12345, 123, 123454321, 123432, 123, 8908908, 123456765432123454321, 123432123, 1234321, 12321]
for i in range(len(num)-1, -1, -1):
    print(i, num[i])
    
num = [12345, 123, 123454321]
sum = 0
for i in num:
    sum = sum+i
print("The entire sum of the code is", sum)

def add(num):
    sum = 0
    for i in num:
        sum = sum+i
    return sum
        
num = [2 ,4 ,5,10]
s1 = add(num)
print(s1)
s2 = add([65, 67, 4345 , 765])
print(s2)

num = [2 ,4 ,5,10]
sum = 0
for i in num:
    sum = sum+i
print(sum)

for i in range(20):
    print(i+1, 'Lohith Thimmichetty is the best pre-teen ever!')
    
print('======================')


for i in range(15):
    print(i+1, 'Lake Stevens is so nice with great schools, and a great community')
    
print('======================')


for i in range(2):
    print(i+1, 'I go to North Lake Middle School in Lake Stevens')

print('======================')

for i in range(2):
    print(i+1, 'I go to North Lake Middle School in Lake Stevens')

for i in range(4):
    print(i+1, 'My name is Lohith Thimmichetty, and I go to North Lake Middle School in Lake Stevens.')

for i in range(6):
    print(i+1, 'I live in the Timber at Lake Stevens. There are 4 phases in the Timbers, Alder, First Phase, Cedar, and Hemlock. I live in the Alder phase.')

for i in range(4):
    print(i+1, "I hate Tanush Thimmichetty! My younger brother by 2 years! I was born 2010, my brother was born 2012,")
'''
for i in range(5):
    print(i+1, "I love my school, North Lake Middle School. NLMS is having its ASB elections right now and we get to be a part of it.")