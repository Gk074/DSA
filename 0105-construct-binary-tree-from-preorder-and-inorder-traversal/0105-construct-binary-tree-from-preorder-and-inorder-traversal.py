# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        rootval = preorder[0]
        root = TreeNode(rootval)
        mid = inorder.index(rootval)

        left_inorder = inorder[:mid]
        right_inorder = inorder[mid+1:]

        left_size = len(left_inorder)

        left_preorder = preorder[1:1+left_size]
        right_preorder = preorder[1+left_size:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

        