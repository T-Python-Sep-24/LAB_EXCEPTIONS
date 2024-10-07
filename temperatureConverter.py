def celsius_to_fahrenheit(celsius:float)->str:
    """
    The function convert celsius to fahrenheit
    Args:
        celsius(float): The degree in celsius that the user put to convert
    Returns:
        a string with the value followed with the unit of the degree
    """
    fahrenheit = round((celsius * 9/5) + 32,2)
    return f"Temperature in Fahrenheit: {fahrenheit} F"
def fahrenheit_to_celsius(fahrenheit)->str:
    """
    The function convert fahrenheit to celsius
    Args:
        fahrenheit(float): The degree in fahrenheit that the user put to convert
    Returns:
        a string with the value followed with the unit of the degree
    """
    celsius = round((fahrenheit - 32) * 5/9,2)
    return f"Temperature in Celsius: {celsius} C"
def main():
    """
    The function displays what the user see
    Args:
        None
    Returns:
        None
    """
    while True:
        try:
            user_input=input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ').upper()
            degree,unit=user_input.split()
            degree=float(degree)
            if unit!='C'and unit!='F':
                raise TypeError()
        except ValueError:
            print("please Write as in the example a float value then space followed by  'C' for Celsius or 'F' for Fahrenheit.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except Exception as e:
            print(e.__class__)
        else:
            break
    if unit=='C':
        print(celsius_to_fahrenheit(degree))
    elif unit=='F':
        print(fahrenheit_to_celsius(degree))
        
main()