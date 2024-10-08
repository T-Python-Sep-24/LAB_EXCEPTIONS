flag = True

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    print()
    additoin(10, 20)
except NameError as error:
    print()
    print('There is an Exception Raised! of type: ', error.__class__)
    print()
except Exception as e:
    print()
    print(e.__class__)
    print()
else:
    print()
    print('The operation is successful!')
    print()

