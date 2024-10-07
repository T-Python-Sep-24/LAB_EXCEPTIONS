def celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit - 32) * 5/9


def main():

    while True:
        
        userInput = input("Enter a temperature and its unit (e.g., '25 C' or '77 F') : ")

        try:
            temperature,unit = userInput.split()
            temperature = float(temperature)

            if unit == 'C':
               result = celsius_to_fahrenheit(temperature)
               print("Temperature in Fahrenheit: {} F".format(result))

            elif unit == 'F':
                result = fahrenheit_to_celsius(temperature)
                print("Temperature in Celsius: {} C".format(round(result,2)))
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit. Try agian" )
        except ValueError:
            print("Error: Please enter a valid temperature.")
        except TypeError as e:
            print(e)

main()