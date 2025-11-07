import time

while True:
    mt = int(input("Enter seconds: "))
    if mt > 0:
        break

for i in range(mt,-1,-1):
    hou = int(i / 3600)
    minu = int(i / 60 - (hou * 60))
    sec = i % 60
    print(f"{hou:02}:{minu:02}:{sec:02}")
    if i == 0:
        print("Time is up!")
    else:
        time.sleep(1)