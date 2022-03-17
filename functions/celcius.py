#Dont Repeat Yourself (DRY    )
  

def temp(celcius):
     
    temper = float(celcius)

    return (f' your temperature in ',abs((temper * 1.8) + 32), 'degrees Faregnheight')

print(temp(24))