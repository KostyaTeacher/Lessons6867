#ТАК НЕ РОБІТЬ НІКОЛИ ❌❌❌❌❌❌❌
        #  0  1  2  3
my_list = [1, 2, 3, 4]
my_list2 = my_list.copy()
for number in my_list:
    print(number)
    if number == 2:
        my_list.remove(number)
print(my_list)
print(my_list2)