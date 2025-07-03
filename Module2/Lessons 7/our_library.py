def calculate(a, b):
    return a + b
print(__name__)

if __name__ == '__main__':
    print(calculate(50, 50))

while True:
    answer = input("Input number")
    if answer.isdigit():
        sum = int(answer) + int(answer)
        print(sum)
        break
    else:
        print("Це не цифра")
        continue

