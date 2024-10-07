def additoin(x, y):

    x = 10
    y = 20
    print("Addition:", x + b)  

try:
    additoin(10, 20)
# Handling NameError exception because 'b' is not defined
except NameError:
    print("NameError occurred. The variable 'b' is not defined.")
else:
    print("The operation is successful")