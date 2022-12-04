#Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
#По графику определите, при каких значения x значение функции отрицательно.

# Дана функция f(x) = -5x^2+10x-30

# 1 Опоределить корни

from sympy import *

x = Symbol('x')
func=-5*x**2+10*x-30
y=solve(func)
x1=float(y[0])
x2=float(y[1])
print(x1,x2)

# 2 Найти интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))

# 3 Найти интервалы, на которых функция убывает

print(solve(fd<0))

# 4 Построить график

import matplotlib.pyplot as plt
list_y=[]
for i in range(1,-25):
    x=i
    y=-8*x**2+3*x+17
    list_y.append(y)
print(list_y)

# 5 Вычислить вершину

corni=solve(fd)
top=corni[0]
x=top
y=-5*x**2+10*x-30
print(top,y)

# 6 Определить промежутки, на котором f > 0

solve(0<func)

# 7 Определить промежутки, на котором f < 0

solve(func<0)
