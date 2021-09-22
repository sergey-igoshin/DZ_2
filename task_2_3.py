"""
DZ 3. *(вместо задачи 2)
Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
чем может сначала показаться.
"""
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = ''

for item in my_list:
    if item.find('+') != -1 or item.find('-') != -1:
        temperature = list(item)
        if len(temperature) > 2:
            item = ('"' + ''.join(temperature) + '"')
        else:
            item = f'"{item[0]}{item[1].zfill(2)}"'
    elif item.isdigit():
        item = f'"{item.zfill(2)}"'

    message += item + ' '

print(message)
