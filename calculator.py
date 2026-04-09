n1= int(input("Enter first number:"))
n2= int(input("Enter second number:"))

def add(x,y):
  return x+y
def subtract(x,y):
  return x-y 
def multiply(x,y):
  return x*y
def divide(x,y):
  if y == 0:
    return "Error: Division by zero is not allowed."
  else:
    return x/y
  
while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  choice = int(input("Enter choice (1/2/3/4/5): "))
  if choice == 1:
    print(n1 ,"+",n2,"=", add(n1,n2))
  elif choice == 2:
    print(n1 ,"-",n2,"=", subtract(n1,n2))
  elif choice == 3:
    print(n1 ,"*",n2,"=", multiply(n1,n2))
  elif choice == 4:
    print(n1 ,"/",n2,"=", divide(n1,n2))
  elif choice == 5:
    print("Exiting the calculator. Goodbye!")
    break
  else:
    print("Invalid input. Please enter a number between 1 and 5.")
  