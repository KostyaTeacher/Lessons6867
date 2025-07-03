while True:
    try:
        answer1 = int(input("Ведіть число 1 "))
        answer2 = int(input("Ведіть число 2 "))
        c = answer1 + answer2
        print(c)
    except ValueError as error:
        print("Це не є числом")
        print(error)
    finally:
        print("Мені було приємно працювати із тобою! Гарного тобі дня !")
