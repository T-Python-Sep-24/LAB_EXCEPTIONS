flag = True
try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + y)

    print()
    additoin(10, 20)
except Exception as error:
    print()
    print('Exception Raised! of type: ', error.__class__)
else:
    print('The operation is successful!')
    print()
    flag = False
finally:
    if flag:
        def correct_additoin(x, y):
            x = 10
            y = 20
            print("Addition:", x + y)

        print()
        print('The Exception handled and corrected successfully, and the addition is:')
        correct_additoin(10, 20)
        print()
    else:
        print('There is no Exception happened')
        print()