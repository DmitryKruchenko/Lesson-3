def my_summs(var):
    return sum(var)

def str_to_num(var):
    var = var.strip()
    if '.' in var and var.replace('.', '').isdigit():
        return float(var)
    elif var.isdigit():
        return int(var)

my_summ = 0
num = 0
j = 0
num_list = []
while j != 1:
    str = (input('Выход - Q: \n Введите любые числа через пробел: '))
    for i in str:
        if (i.upper() == 'Q'):
            j = 1
            break
        n = str_to_num(i)
        if n is not None:
            num_list.append(str_to_num(i))
    if j == 1:
        break
    num += 1


