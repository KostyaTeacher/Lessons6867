fruits = {"яблуко", "банан", "апельсин", "банан", "яблуко"} #множина
print(fruits)
a = set("Kostyao")
b = set("184827374562378656")
print(a)
print(b)
fruits.add("кавун")
fruits.add("драгонфрукт")
print(fruits)
fruits.remove("кавун") #видаляє, викликає помилку якщо єлемента немає
fruits.discard("молоко") #видаляє, не викликає помилку якщо єлемента немає
