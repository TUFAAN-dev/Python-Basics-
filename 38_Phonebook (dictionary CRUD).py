phonebook = {
      "Danish": {
            "Name": "Danish",
            "Numbers": "0001"
      },

      "Arif": {
            "Name": "Arif",
            "Number": "0002"
      },

      "Adil": {
            "Name": "Adil",
            "Number": "0003",
      }
}

while True:
      cmd = input("Command (Add/Lookup/Edit/Delete/Quit): ").lower()
      if cmd == "add":
            name = input("Name: ")
            number = input("Number: ")
            phonebook[name] = number
      elif cmd == "lookup":
            name = input("Name: ")
            print(phonebook.get(name, "Not found"))
      elif cmd == "delete":
            name = input("Name: ")
            phonebook.pop(name, None)
      elif cmd == "edit":
            name = input("Name: ")
            number = input("Number: ")
            phonebook.pop(name, None)
            print(input("Add new Name: "))
            print(input("Add new Number: "))
            phonebook[name] = number
      elif cmd == "quit":
            break
