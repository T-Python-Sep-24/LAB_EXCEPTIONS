def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def main():
    while True:
        enter_temp= input("enter temp and unit: ")
        try:
            temp1,unit = enter_temp.split()
            temprature =float(temp1)
            if unit.upper()=='C':
                convert1= celsius_to_fahrenheit(temprature)
                print(f"Temperature in Fahrenheit: {convert1:.2f} F")
            elif unit.upper()=="F":
                convert1=fahrenheit_to_celsius(temprature)
                print(f"Temperature in Celsius: {convert1:.2f} C")
            else:
                raise TypeError("invalid unit")
        except ValueError:
            print("Invalid temperature value. Please enter a numeric value.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()