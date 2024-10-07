def additoin(x, y):
    try:
        print("additoin:", x + y)
        print("the operation is successful")
    except NameError as e:
        print(e)

    except Exception as e:
        print("something went wrong",e)
additoin(10, 20)

