def name():
  print("Hello, how much is the vibration machine?")
  original_cost = input()
  print("What is the percentage of the discount?")
  discount = input()
  percentage = int(discount)/100
  discount2 = int(original_cost)*float(percentage)
  print("The discount of the machine is", discount2)
  total = int(original_cost)-int(discount2)
  print("The final price of the machine is", total)
  print("What is the cost of the temperature machine?")
  temperature_machine = input()
  print("What is the cost of the thermal shock machine?")
  thermal_machine = input()
  cost_of_both = int(temperature_machine)+int(thermal_machine)
  print("The cost of both machines is", cost_of_both)
  print("What is the discount percentage?")
  discount3 = input()
  percentage2 = int(discount3)/100
  discount4 = int(cost_of_both)*float(percentage2)
  print("The discount of both machines is", discount4)
  total2 = int(cost_of_both)-int(discount4)
  print("The final price of both machines is", total2)
  total3 = int(original_cost)+int(temperature_machine)+int(thermal_machine)
  print("The total cost of the three machines without a discount is", total3)
  total_discount = int(total)+int(total2)
  print("The total cost of the three machines with a discount is", total_discount)

name()
