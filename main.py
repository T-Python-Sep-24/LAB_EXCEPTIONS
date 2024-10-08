#LAB_EXCEPTIONS

def additoin(x, y):
    try:
   
        x = 10
        y = 20
        print("Addition:", x + b)
        print("the operation is successful")
  
    except NameError as a :
        print(f"Operation failed:{a}")
    
     
additoin(10, 20)

print(""*15)

#bouns

def celsius_to_fahrenheit(celsius):
    return  (celsius * 9/5) + 32
  
  
  
def fahrenheit_to_celsius(fahrenheit):
    return  (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            user=input("enter a temperature and its unit ('25 C' or '77 F'): ")

            temp_s,unit=user.split()

            temp = float(temp_s)
           
            if unit.upper()=='C':
                convert_temp = fahrenheit_to_celsius(temp)
                print(f"Temberature in fahrenheit: {convert_temp:.2f}F")
            elif unit.upper()=='F':
                convert_temp = celsius_to_fahrenheit(temp)
                print(f"temberature in Celsius: {convert_temp:.2f}C")
            else:
                raise TypeError(print("Please use 'C' for Celsius or 'F' for Fahrenheit.")) 
            break   

        except ValueError:
            print("Invalid temperature value. Please enter a valid number")

       
        except Exception as e:
            
            print(f"An unexpected error occurred: {e}")
        

main()
