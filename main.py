'''
Lab Exceptions
'''

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as e:
    print("there is name not defiend")    
except Exception as e:
    print(e.__class__)
else:
    print("the operation is successful")
