numbers = [3,1,4,1,5,9]

#Manual loop
max_val = numbers[0]
min_val = numbers[0]
for n in numbers:
      if n > max_val:
            max_val = n
      if n < min_val:
            min_val = n
print(max_val, min_val)

#using built-ins
print(max(numbers), min(numbers))