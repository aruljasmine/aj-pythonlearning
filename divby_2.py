a = int(input("enter the number:"))

for i in range(1, 11):
    if i % 2 == 0:
        print(a, "x", i, "=", a * i)