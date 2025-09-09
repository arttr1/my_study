# def str_to_list(paper: str) -> list[str]:
#     lines = paper.split('\n')
#     matrix = [list(line) for line in lines]
#     return matrix[:len(matrix) - 1]

# def find_symbol(matrix: list[str], symbol: str) -> tuple[int, int]:
#     for i in range(len(matrix)):
#         if symbol in matrix[i]: return (i, matrix[i].index(symbol))
#     return None

# def horizontal_connect(i: int, j1: int, j2: int, matrix: list[str]) -> list[str]:
#     for j in range(j1, j2 + 1):
#         matrix[i][j] = '*'
#     return matrix

# def vertical_connect(j: int, i1: int, i2: int, matrix: list[str]) -> list[str]:
#     for i in range(i1, i2 + 1):
#         matrix[i][j] = '*'
#     return matrix

# def diagonal_connect(j1: int, j2: int, i1: int, i2: int, matrix: list[str]) -> list[str]:
#     if i1 < i2:
#         if j1 < j2:
#             j = j1
#             for i in range(i1, i2 + 1):
#                 matrix[i][j] = '*'
#                 j += 1
#         if j1 > j2:
#             j = j1
#             for i in range(i1, i2 + 1):
#                 matrix[i][j] = '*'
#                 j -= 1
#     if i1 > i2:
#         if j1 > j2:
#             j = j2
#             for i in range(i2, i1 + 1):
#                 matrix[i][j] = '*'
#                 j += 1
#         if j1 < j2:
#             j = j2
#             for i in range(i2, i1 + 1):
#                 matrix[i][j] = '*'
#                 j -= 1
#     return matrix

# def connect_the_dots(paper):
#     matrix = str_to_list(paper)
#     indexes = [find_symbol(matrix, chr(_)) for _ in range(ord('a'), ord('z')+1)]



#     for index in range(1, len(indexes)):
#         if indexes[index] != None:
#             if indexes[index][0] == indexes[index - 1][0]: 
#                 horizontal_connect(indexes[index][0], min(indexes[index - 1][1], indexes[index][1]), max(indexes[index - 1][1], indexes[index][1]), matrix) 
#             elif indexes[index][1] == indexes[index - 1][1]:
#                 vertical_connect(indexes[index][1], min(indexes[index - 1][0], indexes[index][0]), max(indexes[index - 1][0], indexes[index][0]), matrix)
#             elif abs(indexes[index][1] - indexes[index - 1][1]) == abs(indexes[index][0] - indexes[index - 1][0]):
#                 diagonal_connect(indexes[index - 1][1], indexes[index][1], indexes[index - 1][0], indexes[index][0], matrix)
#     s = ''
#     for line in matrix:
#         s += (''.join(line) + "\n")
#     return s 



# s = (
#             "           \n" +
#             "     a     \n" +
#             "    e      \n" +
#             "           \n" +      
#             "  d     b  \n" +
#             "           \n" +      
#             "           \n" +
#             "     c     \n" +
#             "           \n")

# print(connect_the_dots(s))


import numpy as np
import matplotlib.pyplot as plt

# Параметры
R = 0.1  # радиус шара, м
rho = 1e-8  # объёмная плотность заряда, Кл/м^3
k = 8.99e9  # 1/(4 * pi * epsilon_0), Н·м^2/Кл^2
Q = rho * (4/3) * np.pi * (R ** 3)  # общий заряд шара

# Создание массива расстояний r (от 0 до 0.3 м для наглядности)
r = np.linspace(0, 0.3, 1000)
E = np.zeros_like(r)  # массив для напряжённости

# Вычисление E(r)
for i in range(len(r)):
    if r[i] < R:
        E[i] = (rho * r[i]) / (3 * 8.85e-12)
    else:
        E[i] = k * Q / (r[i] ** 2)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(r, E, label='$E(r)$')
plt.axvline(x=R, color='r', linestyle='--', label=f'$r = R = {R}$ м')
plt.scatter([R], [k * Q / (R ** 2)], color='red', zorder=5, label=f'$E(R) \\approx 37.66$ Н/Кл')
plt.xlabel('$r$ (м)')
plt.ylabel('$E$ (Н/Кл)')
plt.title('Зависимость напряжённости электростатического поля $E(r)$')
plt.grid(True)
plt.legend()
plt.show()