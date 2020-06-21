# 125. Valid Palindrome

class Solution:
    def findRelativeRanks(self, nums):
        score_order = sorted(nums, reverse=True)
        dic = {}
        for index, value in enumerate(score_order, 1):
            if index == 1:
                dic[value] = 'Gold Medal'
            elif index == 2:
                dic[value] = 'Silver Medal'
            elif index == 3:
                dic[value] = 'Bronze Medal'    
            else:
                dic[value] = str(index)       

        for index, value in enumerate(nums):
            nums[index] = dic.get(value)
        return nums


# ans = Solution().findRelativeRanks([5,8,1,2,7])
ans = Solution().findRelativeRanks([6,4,3,8,1])
print(ans)

# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.
