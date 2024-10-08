#1. Write functions to convert tempratures

def fahrenheitToCelsius(fahrenheit: float) -> float:
    '''
    This function takes temprature as Fahrenheit and converts it to Celsius
    Args:
        fahrenheit (float): temprature value in Fahrenheit degrees
    Return:
        Temprature value in Celsius
    '''

    return round((fahrenheit - 32 ) * (5 / 9), 2)

def celsiusToFahrenheit(celsius: float) -> float:
    '''
    This function takes temprature as Celsius and converts it to Fahrenheit
    Args:
        celsius (float): temprature value in Celsius degrees
    Return:
        Temprature value in Fahrenheit
    '''

    return round((celsius * (9 / 5)) + 32, 2)

def main():
    '''
    Function in which the main program runs
    '''
    print("----Welcome to Temprature Converter----")

    while True:
        try:
            userInput: str = input("Please enter a temprature followed by an 'F' for Fahrenhite and 'C' for Celsius: ")
            temprature = userInput.split(" ")
            value, unit = temprature

            #Making sure the value entered is a floating point number 
            if not value.replace(".", "").isdigit() and not value.replace("-","").isdigit():
                raise ValueError("This is not a valid temprature. Please try again.")
            
            #If the unit is neither C or F raise a TypeError Exception
            elif unit.upper() != "C" and unit.upper() != "F":
                raise TypeError("Invalid unit entered. Unit should be 'C' for Celsius or 'F' for Fahrenheit.")
            
            #ُIf all the above conditions are false that means there is no exception, 
            #so execute the conversion by calling the methods
            else:
                if unit.upper() == "C":
                    print(f"Temprature in Fahrenheit is: {celsiusToFahrenheit(float(value))} F")
                    break
                if unit.upper() == "F":
                    print(f"Temprature in Celsius is: {fahrenheitToCelsius(float(value))} C")
                    break
        #Handling Exceptions        
        except ValueError as e:
            print(e)
            input("")
        except TypeError as e:
            print(e)
            input("")  
        except Exception as e:
            print(e)
            input("")

#Invoke main function
main()
