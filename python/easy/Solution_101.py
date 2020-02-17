# 101. Symmetric Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.right:
            return self.checktree(root.left, root.right)
        elif root.left or root.right:
            return False
        return True

    def checktree(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.checktree(node1.left, node2.right) \
            and self.checktree(node1.right, node2.left)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            nodes = []
            nodes.append(root)
            count = -1
            while nodes:
                value_li = []
                temp_nodes = []
                for i in nodes:
                    if i:
                        count += 1
                        value_li = self.add(
                            value_li, i.val) if i else self.add(value_li, None)
                        temp_nodes = self.add(
                            temp_nodes, i.left) if i.left else \
                            self.add(temp_nodes, None)
                        temp_nodes = self.add(
                            temp_nodes, i.right) if i.right else \
                            self.add(temp_nodes, None)
                    else:
                        value_li = self.add(value_li, None)
                        # for left and right
                        temp_nodes = self.add(temp_nodes, None)
                        temp_nodes = self.add(temp_nodes, None)
                if not value_li == value_li[::-1]:
                    return False
                if count % 2 != 0:
                    return False
                check = []
                for i in temp_nodes:
                    if i:
                        check.append(1)
                    else:
                        check.append(None)
                if not check == check[::-1]:
                    return False
                nodes = list(filter(lambda v: v is not None, temp_nodes))
                if len(nodes) == 0:
                    return True
                count = 0
        return True

    def add(self, li, data=None):
        if data or data == 0:
            li.append(data)
        else:
            li.append(None)
        return li


# root = TreeNode(1)
# root1 = TreeNode(2)
# root2 = TreeNode(2)
# root3 = TreeNode(3)
# root6 = TreeNode(3)
# root.left = root1
# root.right = root2
# root.left.left = root3
# root.left.right = None
# root.right.left = None
# root.right.right = root6

# [1,2,2,null,3,null,3]
root = TreeNode(1)
root1 = TreeNode(2)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(3)

root.left = root1
root.right = root2
root.left.left = None
root.left.right = root3
root.right.left = None
root.right.right = root4

ans = Solution().isSymmetric(root)
print(ans)
