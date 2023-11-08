import matplotlib.pyplot as plt
import numpy as np

f = np.linspace(-5, 5, 41)
a1 = (f ** 1 + 1 ** 1) / (f ** 1)
a2 = (f ** 1 + 2 ** 1) / (f ** 1)
a3 = (f ** 2 + 1 ** 2) / (f ** 2)

plt.plot(f, a1, color='yellow', linestyle='solid', label='z(X) for: p = 1, n = 1')
plt.plot(f, a2, color='red', linestyle='solid', label='z(X) for: p = 2, n = 1')
plt.plot(f, a3, color='blue', linestyle='solid', label='z(X) for: p = 1, n = 2')
plt.grid()
plt.title(r'Graphic z(f) = (x^n + p^n)/(f^n)')
plt.legend(loc='upper right')
plt.ylabel('z(f)', fontsize=20)
plt.xlabel('f', fontsize=20)
plt.show()

#task4

#4-1
# import matplotlib.pyplot as plt
# import numpy as np
# vals = [48.6, 48.3, 1.99, 0.565, 0.543]
# explode = (0, 0, 0, 0, 0)
# labels = ['none', "towards data science", "the reality project", "noteworthy", "engeeniering"]
# dpi = 100
# fig, ax = plt.subplots()
# ax.pie(vals, explode=explode, startangle=-70, autopct='%1.1f%%', radius=1 )
# ax.axis("equal")
# plt.legend(loc='upper right', labels=labels)
# plt.title(r'Percentage of words by publication')
# plt.show()

#4-2
# import numpy as np
# import matplotlib.pyplot as plt
# x = [10, 15, 20, 25, 30, 35]
# y = [0.00, 0.03, 0.08, 0.05, 0.01, 0.025]
# fig = plt.figure()
# plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
# plt.grid(True)
# plt.show()



#task5
# from random import randint
# from operator import mul
# from functools import reduce
#
# def mprint(matrix):
#     for row in matrix:
#         for item in row:
#             print(f'{item:>3}', end=' ')
#         print()
# n = int(input('Size:\n '))
# matrix = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
# mprint(matrix)
# print()
# tmatrix = list(zip(*matrix))
# ps = [reduce(mul, row) for row in tmatrix]
# min_p = min(ps)
# idx = ps.index(min_p)
#
# if idx < n - 1:
#     tmatrix[idx], tmatrix[idx + 1] = tmatrix[idx + 1], tmatrix[idx]
# else:
#     tmatrix[idx], tmatrix[idx - 1] = tmatrix[idx - 1], tmatrix[idx]
# matrix = list(zip(*tmatrix))
# mprint(matrix)
