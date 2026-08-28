PASSWORD_1 = "secret"
PASSWORD_2 = "danish"
max_attempts = 3

for attempt in range(max_attempts):
      pwd = input("Password: ")
      if (pwd == PASSWORD_1.lower() or pwd == PASSWORD_2.lower()):
            print("Welcome!")
            break
      print(f"Incorrect. {max_attempts - attempt - 1} attempts left.")
else:
      print("Account locked.")

