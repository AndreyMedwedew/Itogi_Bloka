# Задача: Написать программу, которая из имеющегося массива строк формирует массив строк, 
# длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры, 
# либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться 
# коллекциями, лучше обойтись исключительно массивами.

first = ['hello', '2', 'world', ':-)']
second = ['1234', '1567', '-2', 'computer science']
third = ['Russia', 'Denmark', 'Kazan']

def no_more_than_3(some_list):
    res =[]
    for i in some_list:
        if len(i) < 4:
            res.append(i)
    return res

print(no_more_than_3(first))
print()
print(no_more_than_3(second))
print()
print(no_more_than_3(third))