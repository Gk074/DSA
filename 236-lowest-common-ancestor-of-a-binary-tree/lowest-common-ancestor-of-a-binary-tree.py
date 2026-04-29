# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def find_path(node, target, path):
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if find_path(node.left, target, path) or find_path(node.right, target, path):
                return True

            path.pop()
            return False

        path_p = []
        path_q = []

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        lca = None
        i = 0

        while i < len(path_p) and i < len(path_q):
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break
            i += 1

        return lca
        