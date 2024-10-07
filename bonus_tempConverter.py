class wrongSpacingError(Exception):
    """ raised when there is no space between temprature and unit"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    convert Celsius temperature to the equivalent temperature in Fahrenheit

    Args:
        celsius (float): temperature in Celsius

    Returns:
        float: the equivalent temperature in Fahrenheit

    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    convert fahrenheit temperature to the equivalent temperature in Celsius

    Args:
        fahrenheit (float): temperature in fahrenheit

    Returns:
        float: the equivalent temperature in Celsius

    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    """
    Prompts the user for a temperature and its unit then convert it 
    to opposite unit by calling the approprite function

    """
    # prompt for input
    userInput = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')

    # Splits the input into a tempValue and a unit. And catch wrong spacing error
    if len(userInput.split()) != 2:
        raise wrongSpacingError("Should have one space between temprature and unit")
    else: 
        temp, unit = userInput.split()

    # catch wrong input errors raise error if temprature not in digit 
    # use lstrip to remove minus sign (-). isdigit accept only digit
    if not temp.lstrip("-").isdigit():
        raise ValueError("Temprature must be in digit")
    # raise error if unit not 'F' or 'C'
    elif unit.lower() != 'f' and unit.lower() != "c":
        raise TypeError('Unit should only be one letter: "F" or "C"')

    # convert the temperature to its opposite unit using the appropriate function
    if unit.lower() == "c":
        convertedTemp = celsius_to_fahrenheit(float(temp))
        print(f"Temperature in Fahrenheit: {convertedTemp:.2f} F")
    elif unit.lower() == "f":
        convertedTemp = fahrenheit_to_celsius(float(temp))
        print(f"Temperature in Celsius: {convertedTemp:.2f} C")
    input("")

while True:
    try:
        main()
    except ValueError as e:
        print(f"Value Error: {e}")
        input("")
    except TypeError as e:
        print(f"Type Error: {e}")
        input("")
    except wrongSpacingError as e:
        print(f"Wrong Spacing Error: {e}")
        input("")
    except Exception as e:
        print(f"Something went wrong: {e.__class__}")
        input("")
    