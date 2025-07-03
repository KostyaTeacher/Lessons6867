with open("index.txt", "r", encoding="utf-8") as file:
    answer = file.readlines()
sum = 0
for a in answer:
    for chars in a:
        sum += 1

print("Строк", len(answer))
print("Символів", sum)