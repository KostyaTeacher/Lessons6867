#filter
#map
#lambda
fruits = ["banana", "apple", "watermelon", "barbaris", "pamelo", "brokoly"]

numbers = [2, 5, 7, 67, 89, 10, 32, 23, 11, 4, 6]

new_fruits = list(filter(lambda fruit: fruit.startswith("b"), fruits))
print(new_fruits)

new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)