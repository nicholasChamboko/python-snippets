students = ['Nicholas' , 'Mpumelelo','Gareth']
names = ['Chamboko','Dhlula','Maturure']



def named(i, j):
    for i,j in zip(students, names):
        print('Hey there {0}, {1}'.format(i,j))

named(students, names)