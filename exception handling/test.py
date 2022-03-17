#Don't Repeat Yourself

def test(divideBy):
    try:
        return int(30 / divideBy)
    except:
        print('Error: Invalid Argument')

print(test(10))
print(test(5))
print(test(0))
print(test(20))