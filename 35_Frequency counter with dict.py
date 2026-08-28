words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for w in words:
      freq[w] = freq.get(w,0) + 1
print(freq)