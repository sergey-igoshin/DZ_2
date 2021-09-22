"""
DZ 5.Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

a. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если,
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
"""
my_list = [57.8, 46.51, 97, 2558566.45, 110.67, 1.12, 0.78, 1000, 256.45, 45.5, 0.2, 34000]
message = ''

for num in my_list:
    price = str(float(num)).split('.')
    message += f'{int(price[0]):0,} руб {price[1].ljust(2, "0")} коп'.replace(",", " ")
    if my_list[-1] != num:
        message += ', '
print(f'Цены через запятую в одну строку в виде <r> руб <kk> коп\n{message}\n')

"""
b. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
сортировки остался тот же).
"""
print(f'ID до сортиковки ({id(my_list)})')
my_list.sort()
print(f'ID после сортиковки ({id(my_list)})\n')
print(f'Цены отсортированные по возрастанию \n{my_list}\n')

"""
c. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
"""
new_list = my_list.copy()
new_list.sort(reverse=True)
print(f'Новый список отсортированный по убыванию\n{new_list}\n')

"""
d. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""
price_up = [n for n in reversed(new_list[:5:])]
print(f'Пять самых дорогих товаров по возрастанию \n{price_up}')
