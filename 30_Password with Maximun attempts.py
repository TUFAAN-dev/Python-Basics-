PASSWORD_1 = "secret"
PASSWORD_2 = "danish"
PASSWORD_3 = "alishba"
max_attempts = 3

for attempt in range(max_attempts):
      pwd = input("Password: ")
      if (pwd == PASSWORD_1.lower or PASSWORD_2.lower or PASSWORD_3.lower) :
            print("Welcome!")
            break
      print(f"Incorrect. {max_attempts - attempt - 1} attempts left.")
else:
      print("Account locked.")

