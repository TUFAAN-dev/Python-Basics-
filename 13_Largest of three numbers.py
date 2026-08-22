Num_A = int(input("Enter 1st Number: "))
Num_B = int(input("Enter 2nd Number: "))
Num_C = int(input("Enter 3rd Number: "))

if Num_A >= Num_B >= Num_C:
      largest = Num_A
elif Num_B >= Num_A >= Num_C:
      largest = Num_B
else:
      largest = Num_C

print("Largest is", largest)