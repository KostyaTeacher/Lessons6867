course = {"USD": 0.024, "EUR": 0.020}

while True:
    print("Введіть суму в гривнях для конвертації")
    print("Введіть 0 для виходу")
    print()
    choice = input("Введіть ваш вибір: ")
    if choice.isdigit():
        choice = int(choice)
        if choice != 0:
            print("Введіть валюту для конвертації")
            print("1 - USD")
            print("2 - EUR")
            print("Введіть 0 для виходу")
            print()
            choice2 = input("Введіть ваш вибір: ")
            if choice2.isdigit():
                choice2 = int(choice2)
                if choice2 == 0:
                    break
                elif choice2 == 1:
                    valuta = course["USD"]
                    print(f"Ваші {choice} гривень в USD буде становити {choice * valuta} USD!")
                    print()
                elif choice2 == 2:
                    valuta = course["EUR"]
                    print(f"Ваші {choice} гривень в EUR буде становити {choice * valuta} EUR!")
                    print()
                else:
                    print("Ви не ввели потрібну позицію, спробуйте ще раз!")
                    print()
            else:
                print("Ви не ввели цифру, спробуйте ще раз!")
                print()
        if choice == 0:
            break
    else:
        print("Ви не ввели цифру, спробуйте ще раз!")
        print() 