class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            counter += 1
        return counter

print(Solution().countOperations(2,3))