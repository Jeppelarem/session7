text = "abcdefghjkle"
#for letter in text:
#    print(letter)
i = 0
while i < len(text):
    print(text[i])
    i += 1
i = len(text) - 1
while i >= 0:
    print(text[len(text)-i-1],end="")
    i += 1