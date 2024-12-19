# welcome msg
print("Welcome to python Calculator")
print("Select one operater among them ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")

#input operater
operater = input("Enter operater(1,2,3,4,5):")
#input number
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

#conditional statement
if operater == "1":
  result = num_1 + num_2
  print(f"The result of {num_1} + {num_2} is {result}")
elif operater == "2":
  result = num_1 - num_2
  print(f"The result of {num_1} - {num_2} is {result}")
elif operater == "3":
  result = num_1 * num_2
  print(f"The result of {num_1} * {num_2} is {result}")
elif operater == "4":
  result = num_1 / num_2
  print(f"The result of {num_1} / {num_2} is {result}")
elif operater == "5":
  if num_2 == 0:
    print("Error: Division by zero is not allowed")
  else:
    result = num_1 % num_2
    print(f"The result of {num_1} % {num_2} is {result}")
else:
  print("Invalid operater")

# Goodbye message
print("Thank you for using the Python Calculator!")
