# Global conversion factors - accessible throughout the script
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    # Using global variable directly (no global keyword needed for reading)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    # Using global variable directly (no global keyword needed for reading)
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_temperature_input():
    """
    Get temperature input from user with validation.
    
    Returns:
        float: Valid temperature value
        
    Raises:
        ValueError: If input is not a valid numeric value
    """
    try:
        temperature = float(input("Enter the temperature to convert: "))
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """
    Get unit input from user with validation.
    
    Returns:
        str: Valid unit ('C' or 'F')
    """
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    """
    Main function to run the temperature conversion tool.
    """
    try:
        # Get temperature input
        temperature = get_temperature_input()
        
        # Get unit input
        unit = get_unit_input()
        
        # Perform conversion based on input unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()