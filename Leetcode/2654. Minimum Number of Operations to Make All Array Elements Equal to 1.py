import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count

        total_gcd = 0
        for num in nums:
            total_gcd = math.gcd(total_gcd, num)

        if total_gcd > 1:
            return -1

        min_len = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            if current_gcd == 1:
                min_len = 1
                break

            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])

                if current_gcd == 1:
                    current_len = j - i + 1
                    min_len = min(min_len, current_len)

                    break

        ops_to_create_one = min_len - 1

        ops_to_convert_rest = n - 1

        return ops_to_create_one + ops_to_convert_rest