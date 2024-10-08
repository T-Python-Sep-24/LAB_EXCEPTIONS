def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        try:
            temp = input('Enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F"): ')
            # Extract the numerical part of the temperature and convert it to an integer
            degree = int(temp[:-2])
            i_convention = temp[-1]
            if i_convention.upper() == "C":
                result = celsius_to_fahrenheit(degree)
                print(result)
            elif i_convention.upper() == "F":
                result = fahrenheit_to_celsius(degree)          
                print(result)
            else:
                raise TypeError("Invalid unit. Please use 'C' or 'F'.")    

        
        except TypeError as t:
            print(t)

