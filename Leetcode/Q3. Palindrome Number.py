from sympy import *
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        factors = [2, 3, 5]

        for factor in factors:
            while n % factor == 0:
                n //= factor
        return n == 1