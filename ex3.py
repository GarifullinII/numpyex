import numpy as np

# матрица из 10 нулей
print(np.array([0]*15))

# более быстрые способы по скорости выполнения
print(np.empty(10))
print(np.empty(10, dtype='int16'))
print(np.empty((3, 2), dtype='int16'))

# по диагонали 1, остальные 0
print(np.eye(4))

# квадратная матрица (размерность в ())
print(np.identity(5))

# все 0
print(np.zeros((2, 3, 4)))

# массив из всех 1
print(np.ones([4, 3], dtype='int8'))

# произвольные массивы
print(np.full((3, 2), -1))

# генерация матриц на основе списков или по определенным правилам

# создание матрицы по диагонали с данными элементами 1, 2, 3
print(np.diag([1, 2, 3]))

# в данном случае функция выделяет числа, стоящие по главной диагонали
print(np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))

# расположение элементов по диагонали
print(np.diagflat([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))

# все элементы под главной диагональю равны 1, над 0
print(np.tri(4))
print(np.tri(4, 2))

# приведение существующего, к треугольному виду
b = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(np.tril(b))
print(np.triu(b))
print(np.tril([1, 2, 3])) # треугольная матрица
print(np.tril([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print(np.vander([1, 2, 3]))

# формирование числовых диапазонов
print(np.arange(5)) # с шагом 1
print(np.arange(1, 5)) # диапазон 1 - 4
print(np.arange(1, 5, 0.5)) # с шагом 0.5, работает с вещественными данными

print(np.cos(np.arange(0, np.pi, 0.1)))

print(np.linspace(0, np.pi, 0))
print(np.linspace(0, np.pi, 1))
print(np.linspace(0, np.pi, 2))
print(np.linspace(0, np.pi, 3)) # начальное, конечное и середина интервала от 0 до pi (количество делений)

print(np.logspace(0, 1, 3)) # 1 это 1*10 начальное, конечное и середина интервала от 0 до 1 (количество делений)
print(np.geomspace(1, 4, 3)) # геометрическая прогрессия

# формирование массивов на основе имеющихся данных
c = np.array([(1, 2), (3, 4)])
print(c)
d = np.copy(c) # получение копии массива
print(d)

# с применением функции, создание массива
def getRange(x, y):
    return 100*x + y
f = np.fromfunction(getRange, (2, 2))
print(f)

# массив на основе любого итерируемого объекта
print(np.fromiter("hello", dtype='U1'))

# формирование массива из строк
print(np.fromstring('1, 2, 3', dtype='int16', sep=','))