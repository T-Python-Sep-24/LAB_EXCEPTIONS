def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as e:
    print(f"There is a NameError: {e}")
except Exception as e:
    print(f"An error occured {e.__class__}")
else:
    print("the operation is successful")