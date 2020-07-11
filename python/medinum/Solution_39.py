# 39. Combination Sum


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates, target):
        candidates.sort()
        self.findcombination(candidates, target, [])
        return self.ans

    def findcombination(self, candidates, target, temp_li):
        if target == 0:
            find_ans = temp_li.copy()
            self.ans.append(find_ans)
            return
        for index, candidate in enumerate(candidates):
            if target < candidate:
                return
            else:
                temp_li.append(candidate)
                self.findcombination(candidates[index:], target-candidate, temp_li)
                temp_li.pop()


ans = Solution().combinationSum([5, 3, 2], 8)
print(ans)
