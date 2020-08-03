# Напишите функцию, которая превращает список чисел в список строк.
def str_list(int_list):
    return list(map(str, int_list))
str_list(range (10))