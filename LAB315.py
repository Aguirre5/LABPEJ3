import os
os.system("cls")

# lamba y lambad con map.

sum = lambda a, b: a + b
pot = lambda bas, exp: bas ** exp
print(sum(6, 7))
print(pot(9, 3))

num =  [5, 6, 7]

sup = list(map(lambda v: v ** 2, num))
print (sup)
