x = "I love python! 1!!Hello My name is John"
l1 = []
eid_xar = "0123456789!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\`~"

for i in eid_xar:
    if i in x:
        x = x.replace(i, "")

x = x.split()

for i in x:
    if i.isalpha():
        l1.append(i)

length = len(l1)
if length == 1:
    print("The text contains 1 word.")
else:
    print(f"The text contains {length} words")