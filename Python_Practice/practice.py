# class A:
#     def __init__(self):
#         print("Hello World!")
#
# obj = A()
# print(obj.__str__())
#
# # __init__ avtomatik-chaqiriladi
#
import math


# # Hash
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __hash__(self):
#         return hash(self.name)
#
# p1 = Person("John Doe")
# print(hash(p1))
#
# #  Bool
#
# class Energy:
#     def __init__(self, level):
#         self.level = level
#
#     def __bool__(self):
#         return self.level > 0
#
# e = Energy(0)
# print(bool(e))
#
# # Dir
#
# class Secret:
#     def __dir__(self):
#         return ["you", "found", "secrets"]
#
# print(dir(Secret()))
# Find amicable (friendly) numbers up to a given limit
# import math
#
# def sum_proper_divisors(n):
#     if n <= 1:
#         return 0
#     s = 1
#     root = int(math.sqrt(n))
#     for i in range(2, root + 1):
#         if n % i == 0:
#             s += i
#             other = n // i
#             if other != i:
#                 s += other
#     return s
#
# def amicable_pairs(limit):
#
#     sod = [0] * (limit + 1)
#     for i in range(1, limit + 1):
#         sod[i] = sum_proper_divisors(i)
#
#     pairs = []
#     for a in range(2, limit + 1):
#         b = sod[a]
#         if limit >= b > 0 and b != a:
#             if sod[b] == a:
#
#                 if a < b:
#                     pairs.append((a, b))
#     return pairs
#
# print(amicable_pairs(1000))
