from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for j in range(0,len(nums)-1):
        #     if nums[j] == val:
        #         print(nums[j],nums)
        #         nums.remove(nums[j])
        #         j+=1
        #         print(nums)

        while val in nums:
            nums.remove(val)
        print(len(nums))



print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))