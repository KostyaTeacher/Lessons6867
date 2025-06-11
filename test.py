import random

def ask_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = a + b
    try:
        user_input = int(input(f"Скільки буде {a} + {b}? "))
        if user_input == answer:
            print("✅ Правильно!")
            return True
        else:
            print(f"❌ Неправильно! Правильна відповідь: {answer}")
            return False
    except ValueError:
        print("⚠️ Введи саме число!")
        return False

score = 0

for i in range(3):
    print(f"\nПитання {i + 1}")
    if ask_question():
        score += 1

print(f"\n🏁 Гру завершено! Твій результат: {score}/3")
