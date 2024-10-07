def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

user_input = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
try:
    number, unit = user_input.split()
    number = float(number)

    if unit == "C":
        result = celsius_to_fahrenheit(number)
        print(f"{number}°C is equal to {result:.2f}°F")
    elif unit == "F":
        result = fahrenheit_to_celsius(number)
        print(f"{number}°F is equal to {result:.2f}°C")
    else:
        print("Please enter valid unit ")

except ValueError as e:
    print(f"Invalid input: {e}. Please enter (e.g., 25 C or 77 F).")
except Exception as e:
    print(e)




