rows = int(input("enter a number: "))
if rows < 100:
      for i in range (1,rows+1):
            print(" " * (rows - i) + "*" * (2*i-1))
else:
            print("invalid")