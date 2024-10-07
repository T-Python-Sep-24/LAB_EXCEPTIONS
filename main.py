def addition(x, y):
    x = 10
    y = 20
    try:

        print("Addition:", x + b)
    except NameError as e:
        print("The name of the var is wrong.")
        print(e)
    else:
        print("The operation is successful")
addition(10, 20)
