x = "I love python! 1!!Hello My name is John"
y = ""

for i in x:
    if "a" <= i.lower() <= "z":
        y += i
    else:
        y += " "

x = y
x = x.split()
length = len(x)

if length == 1:
    print("The text contains 1 word.")
else:
    print(f"The text contains {length} words")