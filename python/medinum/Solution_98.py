# 98. Validate Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def ValidBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and\
               self.ValidBST(root.right, root.val, max)
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.ValidBST(root, -2**31, 2**31)

# [10, 5, 20, None, None, 12, 22]
root = TreeNode(10)
root1 = TreeNode(5)
root2 = TreeNode(20)
root3 = TreeNode(12)
root4 = TreeNode(22)
root.left = root1
root.right = root2
root.right.left = root3
root.right.right = root4


ans = Solution().isValidBST(root)
print(ans)
