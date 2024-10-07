def additoin(x, y):
    try:

        x = 10
        y = 20
        print("Addition:", x + c)
    except NameError:
        print("there is a name error in the program try to fix it!")
    except Exception as e:
        print(e.__class__)
    else:
        print("the operation is successful")


additoin(10, 20)