num = int(input("number: "))
total = 0
while num > 0:
      total += num % 10
      num //= 10
print("sum of digits", total)