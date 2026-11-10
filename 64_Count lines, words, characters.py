with open("sample.txt", "r") as f:
      text = f.read()
lines = text.count("\n") + 1
words = len(text.split())
chars = len(text)

print(f"Lines: {lines}, words: {words}, Chars: {chars}")


