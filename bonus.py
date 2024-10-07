'''
# Bonus
##  Temperature Converter

```
Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C
```

'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return str(f"{round(fahrenheit,2) } F")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return str(f"{round(celsius,2)} C")

def main():
    degree=input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
    nANDu=degree.split(sep=" ")
    if not float(nANDu[0]):
        raise TypeError("invalid temperature value, Try again.")
    if nANDu[1] == "F":
        result=fahrenheit_to_celsius(float(nANDu[0]))
    elif nANDu[1] == "C":
        result=celsius_to_fahrenheit(float(nANDu[0]))
    else:
        raise ValueError("Please use 'C' for Celsius or 'F' for Fahrenheit, Try again.")
    return result       

while True:
    try:
        result1=main() 
        result2=result1.split(sep=" ")
    except  ValueError as e :
        print(e)
    except TypeError as e:
        print(e)
        
    else:  
        if result2[1] =="F":
            print(f"Temperature in Fahrenheit: {result2[0]} F")
        elif  result2[1] =="C":
            print(f"Temperature in Celsius: {result2[0]} C")   

