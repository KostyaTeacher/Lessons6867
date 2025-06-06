# love кохати
# key value
# dict dictionary

my_dict = { "name": "Alice",
            "age": 10,
            "city": "Wonderland",
            10: 1000}

print(my_dict["city"]) #Взяти значення, але може викликати помилку якщо ключа немає
print(my_dict.get("country")) #Взяти значення, але не викликає помилку
a = my_dict.get("city", "Ukraine") #Якщо значеня не знайдено, повертає по замовчуванню "Ukraine"

user = {}
user["name"] = "Andriy"
user["age"] = 15
user["name"] = "Kostya"
print(user)
#del user["age"]
age = user.pop("age")
print(user)
print(age)

hobbies = { "Міккі Маус": "грати на гітарі",
            "Губка Боб": "ловити медуз",
            "Пікачу": "боротися зі злодіями",
            "Шрек": "жити в болоті",
            "Ельза": "керувати льодом" }
print(hobbies.get("Пікачу"))
#Завдання
print(hobbies.items()) #1
print(hobbies.keys()) #2
print(hobbies.values()) #3


