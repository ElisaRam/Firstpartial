def name():
  print("What is the distance you traveled in kilometers?")
  distance = input()
  print("What was the amount of fuel consumed in liters?")
  fuel_amount = input()
  total_liters = int(fuel_amount)/int(distance)
  print("The consumption of fuel in liters per kilometer is:",total_liters)
  gallon = int(fuel_amount)/3.78
  mile = int(distance)*0.62
  total_gallons = int(gallon)/int(mile)
  print("The consumption of fuel in gallons per mile is:",total_gallons)

#STEP 2
name()
