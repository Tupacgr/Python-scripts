x = "I love python! 1!!"
l1 = []
eid_xar = "0123456789!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\`~"

for i in eid_xar:
    if i in x:
        x = x.replace(i, "")

x = x.split()

for i in x:
    if i.isalpha():
        l1.append(i)

print(l1)