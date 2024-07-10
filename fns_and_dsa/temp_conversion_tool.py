# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Prompt user for input
    temperature = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    try:
        # Convert input to float
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if unit.upper() == "C":
        # Convert Celsius to Fahrenheit
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")
    elif unit.upper() == "F":
        # Convert Fahrenheit to Celsius
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")
    else:
        raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()

# def convert_to_celsius(fahrenheit):
#     fahrenheit = float(input("Enter your fahrenheit value: "))
#     if fahrenheit != str:
#         result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
#         return(result)
#     else:
#         print("Please enter a numeric value: ")
    
# def convert_to_fahrenheit(celsius):
#     celsius = float(input("ENter a celcius value: "))
#     if celsius != str:
#         result = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
#         return(result)
#     else:
#         print("Please enter a numeric value: ")
# convert_to_celsius(fahrenheit)
# convert_to_fahrenheit(celcius)



# def convert_to_fahrenheit(celsius):
#     if not float(temperature):
#         raise TypeError("Invalid temperature. Please enter a numeric value.")
#     elif temperature is float and choice == "F":
#             result = (CELSIUS_TO_FAHRENHEIT_FACTOR * temperature) + 32
#             return result
    
# convert_to_celsius()
# convert_to_fahrenheit()




# def convert_to_celsius(fahrenheit):
#     if not float(temperature):
#         raise TypeError("Invalid temperature. Please enter a numeric value.")
#     elif temperature is float and choice == "C":
#             result = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
#             print(f"{temperature} is {result}")
#     convert_to_celsius(fahrenheit)


    