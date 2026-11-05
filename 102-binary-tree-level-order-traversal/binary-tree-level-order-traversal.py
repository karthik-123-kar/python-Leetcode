# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        r = []
        if root is None:
            return r
        queue = []
        queue.append(root)
        while len(queue)>0:
            temp =[]
            for i in range(len(queue)):
                currnode = queue.pop(0)
                if currnode.left:
                    queue.append(currnode.left)
                if currnode.right:
                    queue.append(currnode.right)
                temp.append(currnode.val)
            r.append(temp)
        return r