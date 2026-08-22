import math

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Choose an operation (1/2/3/4):")
a = float(input("First Number: "))
b = float(input("Second Number: "))

if choice == "1":
      print("Result: ", a + b)
elif choice == "2":
      print("Result: ", a - b)
elif choice == "3":
      print("Result: ", a * b)
elif choice == "4":
      if b != 0:
            print("Result: ", a / b)
      else:
            print("cannot divide by zero")
else:
      print(print("Invalid choice"))
