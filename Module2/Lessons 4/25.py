my_list = []

my_list2 = [1, 5, 78, 23, 45, 67]
#           0          1        2        3         4              5     6
fruits = ["apple", "banana", "chery", "orange", "watermelon", "kiwi"] #dragaonfruit
#            -7       -6        -5     -4           -3         -2     -1
my_list4 = ["Kostya", 20, True, {3, 5, 8}]

print("Index:", fruits[-1])

for number in my_list2:
    print(number)
for fruit in fruits:
    print(fruit.upper())
for item in my_list4:
    print(item)

fruits.append("dragonfruit")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits[-1] = "papaya"
print(fruits)
