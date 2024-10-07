def celsius_to_fahrenheit(celsius):
    '''Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: The converted temperature in degrees Fahrenheit.
    '''
    
    fahrenheit = (celsius * 9/5) + 32.
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    '''
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: The converted temperature in degrees Celsius, rounded to 2 decimal places.

    '''
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)

def test_temperature():
    '''
    Prompts the user to input a temperature and its unit (C or F), 
    then converts it to the opposite unit and displays the result.
    
    The function continues to prompt for input until a valid temperature 
    and unit are entered. Handles exceptions for invalid temperature values 
    and units, printing appropriate error messages.
    '''
    while True:
        try :
            user =  input("Enter a temperature C for Celsius or F for Fahrenheit e.g., 25 C or 77 F:")
            tem,unit= user.split()
            temperature = float(tem)
            
            if unit.lower() == "c":
                convertedFahrenheit = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit:{convertedFahrenheit} F")
                break
            elif unit.lower() == "f":     
                convertedCelsius = fahrenheit_to_celsius(temperature) 
                print(f"Temperature in Celsius: {convertedCelsius}C")
                break
            else:
                raise TypeError
        except ValueError:
            print('Invalid temperature value. Please enter a valid number.')
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("converted temperature and its unit")

test_temperature()
    
