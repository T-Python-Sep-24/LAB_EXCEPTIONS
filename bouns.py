def celsius_to_fahrenheit(celsius):
    """
    this function converts celsius to fehrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    this function converts fehrenheit to celsius 
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def main():
    while True:        
        try:
            temperature= input('enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit): ')
            temp, unit = temperature.split()
            temp = float(temp)
            if  unit.upper()=="C" or unit.upper() == "CELSIUS":
                converted = celsius_to_fahrenheit(temp)
                print(f"the temperature {temp}°C is equal to {converted}°F")
                break
            elif unit.upper()=="F" or unit.upper() == "FEHRENHEIT":
                converted = fahrenheit_to_celsius(temp)
                print(f"the temperature {temp}°F is equal to {converted}°C")
                break
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
                
        except ValueError:
            print("Please don't provide characters. Only valid numbers.")
        except TypeError as e:
            print(e)
main()