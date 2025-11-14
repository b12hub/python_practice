from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) :
        counter_0 = 0
        counter_1 = 0
        result = set()
        for s in sorted(strs) :
            for c in s:
                if c == '0':
                    counter_0 +=1
                    if  counter_0 == m :
                        result.add(s)
                        continue
                elif c == '1' :
                    counter_1 +=1
                    if counter_1 == n :
                        result.add(s)
                        continue
        return counter_0 , counter_1 , len(result)



print(Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3))