# 112. Path Sum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


t = TreeNode(5)
t_l = TreeNode(4)
t_r = TreeNode(8)
t_l_l = TreeNode(11)
t_r_l = TreeNode(13)
t_r_r = TreeNode(4)
t.left = t_l
t.right = t_r
t.left.left = t_l_l
t.right.left = t_r_l
t.right.right = t_r_r

ans = Solution().hasPathSum(t, 17)
print(ans)
