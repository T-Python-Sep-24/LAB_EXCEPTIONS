def celsius_to_fahrenheit(celsius):
    fahrenheit = round((celsius * 9/5) + 32,2)
    return f"{fahrenheit} F"
def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9,2)
    return f"{celsius} C"
def main():
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