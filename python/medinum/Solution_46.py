# 46. Permutations


class Solution:
    def permutation(self, nums, li):
        for i in nums:
            li.append(i)
            subset = nums.copy()
            subset.remove(i)
            if len(subset) == 0:
                self.ans.append(li.copy())
            else:
                self.permutation(subset, li)
            li.pop()

    def permute(self, nums):
        self.ans = []
        li = []
        self.permutation(nums, li)
        return self.ans


ans = Solution().permute([1,2,3])
print(ans)
