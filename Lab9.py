#Lab 9

#The original code raises a NameError because b is used in the additoin function without being defined. This exception occurs when Python cannot find a local or global name.

def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)  # This will raise NameError since 'b' is not defined

    except NameError:
        print("NameError: 'b' is not defined. Please define 'b' and try again.")

    else:
        print("The operation is successful")


additoin(10, 20)
   
   