def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)

    # except Exception as err:
    #     print(err.__class__)
    # it's a NameError
    except NameError:
        print("your have incorrect variable name, please edit fix the problem")
    else:
        print("The operation is successful")


additoin(10, 20)
