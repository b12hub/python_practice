from typing import List

# class Solution:
#     def pivotInteger(self, n: int) -> list[int] | int | None:

        # sum_total_times_two = n * (n + 1)
        # x_squared = sum_total_times_two / 2
        #
        # if x_squared < 0:
        #     return -1
        #
        # x = int(math.sqrt(x_squared))
        # if x * x == x_squared and 1 <= x <= n:
        #     return x
        # else:
        #     return -1

# print(Solution().pivotInteger(8))

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int] | None:
        res = list(range(left, right + 1))
        for i in range(0,len(res)-1):
            if res[i] == 3:
                del res[i]
        return res


print(Solution().selfDividingNumbers(1, 22))