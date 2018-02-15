# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [root]
        zigzag = []
        counter = 0
        while len(stack)!=0:
            inner_list = []
            for i in xrange(len(stack)):
                temp = stack.pop(0)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
                inner_list.append(temp.val)
            if counter%2 == 1:
                zigzag.append(inner_list[::-1])
            else:
                zigzag.append(inner_list)
            counter += 1
        return zigzag