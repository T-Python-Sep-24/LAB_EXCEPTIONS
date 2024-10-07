def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
        try:
            temperature, unit = user_input.split()
            temperature = float(temperature)

            if unit.upper() == 'C':
                converted = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {converted:.2f} F")
            elif unit.upper() == 'F':
                converted = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {converted:.2f} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError:
            print("Invalid temperature value. Please enter a numeric value.")
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
