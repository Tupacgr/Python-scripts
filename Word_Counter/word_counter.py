x = input("Enter the text: ")
y = list()

for i in x:
    if i.isalpha():
        y.append(i)
    elif y and y[len(y) - 1] != " ":
        y.append(" ")

y = "".join(y)
y = y.split()
length = len(y)

if length == 1:
    print("The text contains 1 word.")
else:
    print(f"The text contains {length} words")