import numpy as np

# основные свойства

# текущий типа элементов .dtype
# смена типа .dtype = np.int8()
# размер массива .size
# сколько байт занимает один элемент в массиве .itemsize

a = np.ones((3, 4, 5))
print(a)
# количество осей массива
print(a.ndim)
# число элементов по каждой оси
print(a.shape)
# изменяем размерность и создаем одномерный массив
a.shape = 60
print(a)
# получаем двумерный массив
a.shape = 12, 5

# как узнать, когда создается новый массив, а когда представление view() - возвращает копию его представления
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# ссылка на один и тот же массив
c = b
b.shape = 3, 3
# в больших проектах это приводит к ошибкам, когда на входе ожидает вектор, а получаем матрицу, чтобы избежать данной ошибки создаем новое представление начального массива
c = b.view()
# создание копии данных всего массива, а не представления c = a.copy()
