#Below you have a code that raises an exception , using what you learned do the following:

#Find what type of exception is raised.
#Hanlde the exception in try..except
#If operation successful , print "the operation is successful"
#if operation fails, handle the specific exception that is raised , and print a relevant message.

def addition(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)  # This will raise a NameError
    except NameError as e:
        print("An error occurred: ", e)
    else:
        print("The operation is successful")

addition(10, 20)

