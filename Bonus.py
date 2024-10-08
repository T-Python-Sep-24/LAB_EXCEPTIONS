
def celsius_to_fahrenheit(celsius)->float:
    fahrenheit = (celsius * 1.8) + 32
    return round(fahrenheit, 2)
def fahrenheit_to_celsius(fahrenheit)->float:
    celsius = (int(fahrenheit) - 32)*5/9
    return round(celsius, 2)
def main():
    while True:
        try:
            user_input = input("Enter the temperature and unit (e.g., '25 C' or '77 F'): ")
            temp_value, temp_unit = user_input.split()
            temp_value = float(temp_value)
            if temp_unit=="F":
                temp=fahrenheit_to_celsius(temp_value,)
                print(f"Temperature in Celsius:{temp}C")
            elif temp_unit=="C":
                temp=celsius_to_fahrenheit(temp_value)
                print(f"Temperature in Fahrenheit:{temp}F")
            else:
                raise TypeError("invalid unit")
            break
        except ValueError:
            print("Please enter a temperature in Celsius or Fahrenheit")
        except TypeError as e:
            print(e)
main()
