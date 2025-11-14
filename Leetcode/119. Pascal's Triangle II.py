from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for _ in range(1, rowIndex+1):
            prev = triangle[-1]
            row = [1]
            for i in range(1, len(prev)):
                row.append(prev[i - 1] + prev[i])
            row.append(1)
            triangle.append(row)
        return triangle[-1]