n = int(input("Numbers: "))

fact = 1
i = 1

while i <= n:
      fact *= i
      i += 1
print(f"{n}! = {fact}")


total = 0
while fact > 0:
      total += fact % 10
      fact //= 10
print("Sum of digits", total)