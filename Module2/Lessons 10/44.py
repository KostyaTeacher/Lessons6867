print('долар = 39.45 грн, євро = 42.24 грн')
dollar = 39.45
evro = 42.24

while True:
    print('Обмінник')
    print('1. Перейти до обміну валют')
    print('2. Вийти')

    try:
        answer = float(input('<1>, <2>: '))
    except ValueError:
        print('Помилка! Введіть число 1 або 2.')
        continue

    rahunok = 0

    if answer == 1:
        print('1. Обміняти гривні на долари')
        print('2. Обміняти долари на гривні')
        print('3. Обміняти гривні на євро')
        print('4. Обміняти євро на гривні')
        print('5. Вийти')

        try:
            option = int(input('Виберіть опцію: '))
        except ValueError:
            print('Помилка. Введіть число від 1 до 5.')
            continue

        if option == 1:
            while True:
                try:
                    grivni = int(input('Внесіть гривні до ячейки. 0 — Вийти: '))
                except ValueError:
                    print('Помилка. Введіть число.')
                    continue
                if grivni == 0:
                    break
                dollars = round(grivni / dollar, 2)
                rahunok += dollars
                print('Ви отримали', dollars, 'доларів')
                print('На вашому рахунку', rahunok, 'доларів')
            print('Отримайте ваші', rahunok, 'дол. в щілині')

        elif option == 2:
            while True:
                try:
                    dollars = int(input('Внесіть долари до ячейки. 0 — Вийти: '))
                except ValueError:
                    print('Помилка. Введіть число.')
                    continue
                if dollars == 0:
                    break
                grivni = round(dollars * dollar, 2)
                rahunok += grivni
                print('Ви отримали', grivni, 'гривень')
                print('На вашому рахунку', rahunok, 'гривень')
            print('Отримайте ваші', rahunok, 'грн. в щілині')

        elif option == 3:
            while True:
                try:
                    grivni = int(input('Внесіть гривні до ячейки. 0 — Вийти: '))
                except ValueError:
                    print('Помилка. Введіть число.')
                    continue
                if grivni == 0:
                    break
                evr = round(grivni / evro, 2)
                rahunok += evr
                print('Ви отримали', evr, 'євро')
                print('На вашому рахунку', rahunok, 'євро')
            print('Отримайте ваші', rahunok, 'євро')

        elif option == 4:
            while True:
                try:
                    evr = int(input('Внесіть євро до ячейки. 0 — Вийти: '))
                except ValueError:
                    print('Помилка. Введіть число.')
                    continue
                if evr == 0:
                    break
                grivni = round(evr * evro, 2)
                rahunok += grivni
                print('Ви отримали', grivni, 'гривень')
                print('На вашому рахунку', rahunok, 'гривень')
            print('Отримайте ваші', rahunok, 'грн. в щілині')

        elif option == 5:
            print('До побачення')
            break
        else:
            print('Неправильний вибір. Повторіть спробу.')

    elif answer == 2:
        print('До побачення')
        break
    else:
        print('Неправильний вибір. Повторіть спробу.')