'''
myList = [3, 5, 9, 8]
num_to_find = 5
for number in myList:
    print(number)
    if number == num_to_find :
        print('Number found in the list, breaking ...')
        break

toys = ['Car' , 'Doll', 'Teddy']
i = 0
for toy in toys:
    print(toy)
    continue
    print("I like ", toy)
    
numList=[100, 40, 20, 30, 45, 323, 53]
for number in numList:
    if number % 10 == 0:
        print(number)    
    
fruit = 'Pineapple'
i=0
while i < len(fruit):
    if fruit[i] == 'e':
        print('_', end='')
    else:
        print(fruit[i], end='')
    
    i=i+1

# printing elements at even index
listnum=[11, 22, 33, 44, 55]
i = 0
while i < len(listnum):
    if i%2 != 0:
        print(listnum[i])
    i = i + 1

for i in range(4,8):
    for j in [0, 1, 2]:
        print(i, end=' ')
    print()
  
# Check if there are negative number in the list
def checkNegativeNumbers(listnum):
    for number in listnum:
        if number < 0:
            print('Negative number found in the list')
            break
            
checkNegativeNumbers([2, -4, 5, 6, -3])
checkNegativeNumbers([1, 2, 6])

a_string = "Alabama"
a_string = a_string.replace("a", "o")
a_string = a_string.replace("A", "o")
print(a_string)

num1 = int(input('Enter number 1 '))
num2 = int(input('Enter number 2 '))
print(num1*num2)
print(num1+num2)
print(num1-num2)
print(num1/num2)

if num1== 12:
    print("You have printed 12")
'''

num1 = float(input("Please sumbit your first number here: "))
num2 = float(input("Please sumbit your second number here: "))
print(num1+num2)
print(num1/num2)
print(num1*num2)
print(num1-num2)
if num1 == 12:
    print("Your first answer was 12")
if num2 == 12:
    print("Your second answer was 12")


    
    
    
    
    
    
    
    
    
    