# Запитуємо вираз у користувача

expression = input("Введи математичний вираз: ")

# Обчислюємо вираз за допомогою eval

result = eval(expression)

# Виводимо результат

print(f"Результат: {result}")

while True:

    expression = input("Введи математичний вираз (або 'вихід' для завершення): ")

    if expression.lower() == "вихід":

        break

    result = eval(expression)

    print(f"Результат: {result}")