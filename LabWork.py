#Lab Solution
def addition(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    addition(10, 20)
except NameError as e:
    print("Variable 'b' was not defined")
except Exception as e:
    print(type(e))
    print(e)
else: 
    print("Operation is successful.")