#1

def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("Dame el primer numero:")
a = int(input())
print("Dame el segundo numero:")
b = int(input())
print("La suma da",suma(a,b), "y la resta da",resta(a,b))

#2

def multiplication(a,b):
  x = a*b
  return x

def division(a,b):
  x = a/b
  return x

print("What is the first number?")
a = int(input())
print("What is the second number?")
b = int(input())
print("The multiplication result is",multiplication(a,b), "and the division result is", division(a,b))

#3

def conversion():
  print("How many kilometers have passed?")
  km = int(input())
  m = km*1000
  print("Your distance in meters is", m, "meters")

conversion()

#4

def triangle_area():
  print("What is the base?")
  base = int(input())
  print("What is the height?")
  height = int(input())
  area = (base*height)/2
  print("The area of your triangle is", area)

triangle_area()

#5

