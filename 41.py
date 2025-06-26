user = {}
user["name"] = "Andriy"
user["age"] = 15
user["city"] = "Kherson"
print(user)
print("⭐" * 50)

for k, v in user.items():
    print(f"{k} -> {v}")