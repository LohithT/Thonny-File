'''
score = int(input('Enter the score: '))
print('Score you entered is', score)

if score<=100 and score >=85:
    print('A')
elif score>=70:
    print('B')
elif score>=55:
    print('C')
elif score>=33:
    print('D')
elif score<33:
    print('E')
else:
    print('Invalid Number')

number = int(input('Enter the number: '))
if ( (number >= 5 and number <= 10) or (number >= 15 and number <= 20)):
    print(number, 'is inside 5-10 or 15-20')
else:
    print(number, 'is not inside 5-10 or 15-20')

day_or_night = input("Is it day or night? ")
if day_or_night == "day":
    print('Yes its day')
    morning_or_evening = input("Is it morning or evening? ")
    if morning_or_evening == "morning":
        print("Have your breakfast.")
    else:
        print("Have your dinner.")
    
else:
    print("It's night time. Go to sleep.")

'''
day_or_night = input("Is it day or night? ")
if day_or_night == "day":
    print('It\'s day.')
    morning_or_night_afternoon_or_dusk = input("Is it the morning, afternoon, dusk, or night? ")
    if morning_or_night_afternoon_or_dusk == "afternoon":
        print("Have your lunch and maybe you should consider playing outside.")
    if morning_or_night_afternoon_or_dusk == "morning":
        print("Have your breakfast.")
    if morning_or_night_afternoon_or_dusk == "dusk":
        print("Get ready for bed.")
    if morning_or_night_afternoon_or_dusk == "night":
        print("It's night time. Go to sleep!")
    
























