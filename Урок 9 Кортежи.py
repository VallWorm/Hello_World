# Кортеж меньше потребляет мощности ОЗУ
# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
# print(b.__sizeof__())

# a = (1, 2, 3, 4, 5, 6)
# print(a[0:3])
# print(a[2::2])



#
# a = (10, 2.13, "square", 89, "C")
# b = [1, 2, 3]
# c = list(a)
# d = tuple(b)
# print(c)
# print(d)

# nested = (1, "do", ["param", 10, 20])
# nested[2][1] = 15
# print(nested)

# x = (1, 2, 3, 4)
# z = x * 2
# print(z)

# import random
# a = []
# for i in range(11):
#     a.append(random.randint(0, 100))
# a = tuple(a)
# print('min', min(a), 'max', max(a))

# import random
# a = [random.randint(0,5) for i in range(5)]
# c = [random.randint(-5, 0) for i in range(5)]
# b = tuple(a)
# d = tuple(c)
# e = tuple(a + c)
# print(a,c)
# print(e)

# a = ('Зубенко', 'Михаил', 'Петрович')
# b = ', '.join(a)
# print(b)

# a = (13, 5, 49, 67, 32, 10, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# b = (55, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# c = sum(a)
# d = sum(b)
# if c > d:
#     print('Сумма а больше')
# else:
#     print('Сумма b больше')
# print('min a', min(a), a.index(min(a)))
# print('min b', min(b), b.index(min(b)))
#

# a = [4, 6, 'py', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
#
# a.extend(b)
# a.insert(3,6)
# print(a)
# for i in a:
#     if type(i) is str:
#         a.remove(i)
# a.sort()
# print(a)
