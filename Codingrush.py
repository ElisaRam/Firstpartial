#codingrush
def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
  
def celsius_to_kelvin(celsius):
  kelvin = celsius + 273.15
  return kelvin
celsius_str = input ("Enter temperature in Celsius: ")
celsius = int(celsius_str)

fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celstus_to_kelvin(celsius)

result = f"{celsius]°C is equal to {fahrenheit: .2f]°F\n{celstus]°C is
equal to {kelvin: .2f} K"
                                    
print(result)
