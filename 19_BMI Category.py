Weight = float(input("Weight in kg: "))
Height = float(input("Height in m:"))

bmi = Weight / (Height ** 2)
print(f"BMI = {bmi:.1f}")

if bmi < 18.5:
      print("UnderWeight")
elif bmi < 25:
      print("Normal Weight")
elif bmi < 30:
      print("Over weight")
else:
      print("Obese")