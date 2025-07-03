while True:
    try:
        answer = int(input("Input number > "))
        c = answer + answer
        print(c)
    except ValueError as error:
        print("It`s not number")
        print(error)