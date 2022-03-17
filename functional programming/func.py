def outer():

    def inner():
        print('Inner Function')

    return inner

function = outer()
print(function)
function()

outer()()