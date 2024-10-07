def additoin(x, y):
    try:    
        x = 10
        y = 20
        print("Addition:", x + b)
        print("The operation is successful")
    
    except NameError as error :
        print(f"Operation failed: {error}")
    except Exception as er:
        print("An error occurred")
        print(er.__class__)
    except:  
        print("please check about arguments")
additoin(10, 20)
