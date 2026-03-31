# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        count = {}
        ans = []

        def dfs(node):
            if not node:
                return "#"

            serial = str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

            count[serial] = count.get(serial, 0) + 1
            if count[serial] == 2:
                ans.append(node)

            return serial

        dfs(root)
        return ans