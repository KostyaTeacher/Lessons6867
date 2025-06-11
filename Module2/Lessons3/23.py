def add(a, b, c):
    return a + b + c


add(5, 10, 15)


def add2(a=10, b=20, c=30):
    return a + b + c


def add3(a, b, c=100):
    return a + b + c


print(add2(b=50, a=20))
print(add3(10, 20))

print("Kostya")
