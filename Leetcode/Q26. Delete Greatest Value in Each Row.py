from typing import List

class Solution:
    def deleteGreatestValue(self ,grid: List[List[int]]):

        return [item for item in  range(len(grid)-1,-1 ,-1 )]
obj = Solution()
print(obj.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
