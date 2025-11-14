from typing import List

from PIL.ImageChops import difference


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if 2 <= len(arr) <= 1000:
            arr.sort()
            print(arr)
            nums_dif = arr[0] - arr[1]
            for i in range(1,len(arr)-1):
                if arr[i] - arr[i+1] != nums_dif:
                    return False
                else:
                    return True
            return True
        else:
            return False
print(Solution().canMakeArithmeticProgression([-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1]))