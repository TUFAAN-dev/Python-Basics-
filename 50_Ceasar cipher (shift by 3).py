text = input("Text: ")
shift = 3
encrypted = ""
for ch in text:
      if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            encrypted += chr((ord(ch) - base + shift) % 26 + base)
      else:
            encrypted += ch
print(encrypted)