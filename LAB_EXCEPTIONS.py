
def additoin(x,y):
    try:
        x = 10
        y = 20
        print("Addition : ", x + b) #undefined variable 'b' ,this will raise a NameError
        print("the operation is successful.")
    except NameError as e:
        print("\n NameError:  {}. not defined \n ".format(e))
        
        
additoin(10,20)





