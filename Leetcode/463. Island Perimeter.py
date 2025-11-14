from typing import List

class Solution:
    def islandPerimeter(grid: List[List[int]]) -> int:
        rec_counter = 0
        rows , cols = len(grid) , len(grid[0])
        land  , shared = 0 ,0
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 1:
                    land+=1
                    if r+1 < rows and grid[r+1][c] == 1:
                        shared+=1
        print(land*4 - shared*4)


obj = Solution
print(obj.islandPerimeter([[1]]))
