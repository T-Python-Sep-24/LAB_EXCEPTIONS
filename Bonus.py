#Bonus
def celsius_to_fahrenheit(celsius):
    return (celsius*9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    while True:
            try:
                temperature_in=input("Enter a temperature and its unit ")
                temperature_in=temperature_in.split(" ")
                temperature , unit = float(temperature_in[0]),temperature_in[1].upper()
                if unit =="C":
                    C=round(celsius_to_fahrenheit (temperature),2)
                    print(f"Temperature in Fahrenheit: {C} F")
                elif unit=="F":
                    F=round(fahrenheit_to_celsius (temperature),2)
                    print(f"Temperature in Celsius: {F} C")
                elif unit not in ["C","F"]:
                    raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            except TypeError as err:
                print(err)
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)
main()