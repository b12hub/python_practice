"""Pascal's Triangle"""

import numpy as np

class Solution:
    def generate(self, numRows: int) :
        triangle = [[1]]
        for _ in range(1, numRows):
            prev = triangle[-1]
            row = [1]
            for i in range(1, len(prev)):
                row.append(prev[i - 1] + prev[i])
            row.append(1)
            triangle.append(row)
        return triangle


print(Solution().generate(5))



