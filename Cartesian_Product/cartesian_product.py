from itertools import product

def calc(in_set, el_num):
    cart_prod = product(in_set, repeat = el_num)
    cart_prod = tuple(cart_prod)
    return cart_prod

print("This script finds the Cartesian product of a given set and prints it.")

s1 = set()
while True:
    el = input("Enter one of the set's elements (enter 'q' to quit): ").strip()
    if not (el in ["q", "Q"]):
        el = float(el)
        if int(el) == el:
            el = int(el)
        s1.add(el)
    else:
        break

s1 = tuple(s1)
while True:
    num = int(input("Enter the size of combinations (>1): "))
    if num > 1:
        break
    else:
        print("Should be >1! Please try again.")

res = calc(s1, num)
print(f"The cartesian product of the given set with {num} elements is:", res, sep = "\n")