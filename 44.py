text = input("Input your word ").lower()
for c in text:
    if c in "aeiou":
        text = text.replace(c, "0")
        #print("0", end="")
    elif c in "bcdfghjklmnpqrstvwxyz":
        #print("1", end="")
        text = text.replace(c, "1")

print(text)