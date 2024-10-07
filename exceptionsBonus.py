

def celsius_to_fahrenheit(celsius):
    """
    Function that converts from Celsius to Fahrenheit
    :param celsius
    :return fahrenheit
    """
    fahrenheit = ((9/5) * celsius) + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit):
    """
    Function that converts from Fahrenheit to Celsius
    :param fahrenheit:
    :return celsius
    """
    celsius = (fahrenheit - 32) * (5 / 9)
    return round(celsius, 2)

def app():
    """
    This is the main function that handles user inputs and handle exceptions

    """
    while True:

        try:

            temperature_input = input("Enter the temperature and its unit (e.g. \"35 C\" or \"65 F\") or Q to Quit: ")
            if temperature_input.lower() == "q":
                print("thx")
                break
            tempData = temperature_input.split(" ")
            temp = float(tempData[0])
            unit = (tempData[1]).lower()

            if unit == "c":
                print(f"{temp} in °C equals {celsius_to_fahrenheit(temp)} in F")
            elif unit == "f":
                print(f"{temp} in °F equals {fahrenheit_to_celsius(temp)} in C")
            else:
                raise TypeError
        except IndexError:
            print("Please Enter the complete temperature and its unit")
        except ValueError:
            print("Please Enter valid temperature then its unit separated by a space")
        except TypeError:
            print("This Unit is not supported, Please Enter only the Units C (Celsius) or F (Fahrenheit) ")


app()
