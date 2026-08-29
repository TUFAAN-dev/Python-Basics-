s1 = input("First word: ").lower()
s2 = input("Second word: ").lower()
if sorted(s1) == sorted(s2):
      print("Anagram")
else:
      print("Not Anagram")