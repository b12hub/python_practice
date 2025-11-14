from typing import List

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        from collections import defaultdict

        positions = defaultdict(list)
        for i, val in enumerate(nums):
            positions[val].append(i)

        min_dist = float('inf')
        found = False

        for val, inds in positions.items():
            if len(inds) >= 3:
                # Check all possible triplets of indices
                for a in range(len(inds) - 2):
                    for b in range(a + 1, len(inds) - 1):
                        for c in range(b + 1, len(inds)):
                            i, j, k = inds[a], inds[b], inds[c]
                            dist = abs(i - j) + abs(j - k) + abs(k - i)
                            min_dist = min(min_dist, dist)
                            found = True

        return min_dist if found else -1

print(Solution().minimumDistance([1, 2, 1, 2, 1, 3]))