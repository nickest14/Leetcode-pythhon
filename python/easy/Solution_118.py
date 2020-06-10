# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int):
        ans = []
        for x in range(numRows):
            temp_li = []
            for y in range(x+1):
                if y == 0 or y == x:
                    value = 1
                else:
                    value = ans[x-1][y-1] + ans[x-1][y]
                temp_li.append(value)
            ans.append(temp_li)
        return ans

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
ans = Solution().generate(5)
print(ans)

