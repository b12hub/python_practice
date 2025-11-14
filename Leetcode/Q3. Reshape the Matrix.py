from typing import List
class Solution:
    def matrixReshape(self,mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        if r * c == len(mat) * len(mat[0]):
            return np.array(mat).reshape(r, c).tolist()
        else:
            return mat

obj = Solution()
print(obj.matrixReshape([[1,2],[3,4]] , 1 , 4))