#Bonus Lab 9


def celsius_to_fahrenheit(celsius):
    fahrenheit_result = (celsius * 9/5 + 32)
    return fahrenheit_result

def fahrenheit_to_celsius(fahrenheit):
    celsius_result = (fahrenheit - 32) * 5/9
    return celsius_result

def main():
    while True:
        try:
            # Get user input and split into temperature and unit
            user_temperature = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temp_str, unit = user_temperature.split()
            
            temperature = float(temp_str)
            
            if unit.upper() == "C":
                convert_to_fahrenheit = celsius_to_fahrenheit(temperature)
                print(f"Your Temperature in Fahrenheit: {convert_to_fahrenheit:.2f} F")
                
            elif unit.upper() == "F":
                convert_to_celsius = fahrenheit_to_celsius(temperature)
                print(f"Your Temperature in Celsius: {convert_to_celsius:.2f} C")
                
            else:
                raise TypeError("Invalid Unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            
            break  

        except ValueError:
            print("Invalid Temperature Value. Please Enter a Numeric Temperature.")
            
        except TypeError as t:
            print(t)

main()

 

