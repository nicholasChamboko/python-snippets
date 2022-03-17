#Don't Repeat Yourself

#you put a start next to your parameter if you dont know the number of arguments you are going too recieve
#the arguments will be returned as a turple


def myName(*args): 
    print('My Name is ', args)

myName('Kupakwashe', 'Nicholas', 'Chamboko')