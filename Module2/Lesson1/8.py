name = "Kostya"
name3 = "Buhaiov"
name2 = """Реве та стогне Дніпр широкий,
Сердитий вітер завива,
Додолу верби гне високі,
Горами хвилю підійма.
                І блідний місяць на ту пору
Із хмари де-де виглядав,
Неначе човен в синім морі,
То виринав, то потопав.
                Ще треті півні не співали,
Ніхто нігде не гомонів,
                    Сичі в гаю перекликались,
Та ясен раз у раз скрипів."""
print("*" * 50)
print(name2)
print("*" * 50)
print(name * 10 + name3 * 10)
print((name + name3 + " ") * 10)

answer = "I love Python, very well, love Apple, love Orange"
print(len(answer))

# c = input("Enter password > 8 letters ")
# if len(c) < 8:
#     print("Password short")
# else:
#     print("Password OK")

print(answer.upper())
print(answer.lower())
answer.replace("love", "@")
print(answer)

if answer.count("love") >= 3:
    answer = answer + " " + answer.replace("love", "#####")
print(answer)



