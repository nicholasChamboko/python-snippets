#Don't rpeat yourself

'''if you do know the number of keyword arguments you are to recieve, you add ** before your parameter list 
    the arguments will be recieved as a dictionary
'''

def myName(**myname):
    print(myname)

myName(name='Nicholas', surname = 'Chamboko')