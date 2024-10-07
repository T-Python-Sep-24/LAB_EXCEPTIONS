def main():
    while True:
        try:
            # Prompt user input
            temp_data = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ").strip()

            # Split input into temperature and unit
            temp_value, unit = temp_data.split()

            # Convert temperature value to a float (handling ValueError)
            temp_value = float(temp_value)

            # Check for valid unit and perform conversion
            if unit.upper() == 'C':
                celsius_to_fahrenheit(temp_value)
            elif unit.upper() == 'F':
                fahrenheit_to_celsius(temp_value)
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError:
            print("Invalid temperature value. Please enter a valid number.")
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            break  # Exit loop if conversion was successful

def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f} F")

def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {celsius:.2f} C")

# Call the main function to run the program
main()
