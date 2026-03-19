class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: ;bool
        """
        lst = []
        x = {'[':']', '{':'}', '(':')'}
        for ch in s:
            if ch in x:
                lst.append(ch)
            else:
                if not lst:
                    return False
                top = lst.pop()
                if x[top] != ch:
                    return False
        return len(lst) == 0


