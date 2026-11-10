line = input("Add a line:")
with open("log.txt", "a") as f:
      f.write(line + "\n")


