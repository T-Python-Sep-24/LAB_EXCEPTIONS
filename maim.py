def additoin(x, y):    
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError()
        
    print("Addition:", x + y)

try:
   additoin(10,30)
     
except NameError:
    print("You have an name error Check the numbers")
except ValueError:
    print("ValueError : entr only number ")
except Exception as e:
    print(f"Operation failed due to a : {e.__class__}")
else:
    print("the operation is successful")
