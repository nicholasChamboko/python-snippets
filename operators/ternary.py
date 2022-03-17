from email import message


age = 20

'''if age >= 18:
    print('Can Vote')
else:
    print('Can\t Vote')'''

age = 'Not able to vote' if age <= 18 else "can Vote"

print(age)