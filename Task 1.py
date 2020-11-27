def my_divide(devidend, divisor):

    try:
        result = my_dividend / my_divisor
        return result

    except ZeroDivisionError:
        print('Введите число отличное от 0')



my_dividend = int(input('Введите любое число - делимое: '))
my_divisor = int(input('Введите любое число - делитель: '))

my_result = my_divide(my_dividend, my_divisor)
print(my_result)