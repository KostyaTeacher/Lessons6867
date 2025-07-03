answer1 = input("Input your numbers > ")
if answer1.isdigit():
    print("Це точно число")
try:
    result = int(answer1) / int(answer1)
    print(result)
except ValueError as error:
    print("Це не число")
    print(error)
except ZeroDivisionError as error:
    print("На нуль діліти не можна")
    print(error)
else:
    print("Помилок не було")
finally:
    print("Цей код виконується завжди")