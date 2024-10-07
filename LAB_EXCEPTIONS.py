def addition(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)  # This will raise a NameError
        print("The operation is successful.")
    except NameError as e:
        print(f"Error: {e}. Variable 'b' is not defined.")

# Call the addition function
addition(10, 20)
