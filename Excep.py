def addition(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)  # raising a NameError
        print("The operation is successful")
    except NameError as e:
        print(f"Operation failed: {e}. 'b' is not defined.")

addition(10, 20)
