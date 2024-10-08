def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            temperature = input('Please enter a temperature with its unit: ')
       
            parts = temperature.split()
            temp_str, unit = parts
            temp = float(temp_str)  
            
            if unit.upper() == 'C':
                converted_temp = celsius_to_fahrenheit(temp)
                print(f'The converted temperature from Celsius to Fahrenheit is {round(converted_temp, 2)} F')
            elif unit.upper() == 'F':
                converted_temp = fahrenheit_to_celsius(temp)
                print(f'The converted temperature from Fahrenheit to Celsius is {round(converted_temp, 2)} C')
            else:
                raise TypeError('Invalid unit! Please enter "C" for Celsius or "F" for Fahrenheit')
                
            break
            
        except ValueError:
            print('Invalid temperature value! Please enter a valid number')
        except TypeError as e:
            print(e)

print()
main()
print()