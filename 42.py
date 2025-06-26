for i in range(1, 11):
    print()

    for j in range(1, 11):
        print()
        for k in range(1, 11):
            print()
            if k % 2 == 0:
                continue
            print(f"{i} * {j} * {k} = {i * j * k}", end=" -> ")

