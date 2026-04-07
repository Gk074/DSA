from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        dict1={}
        for i in strs:
            check = ''.join(sorted(i))
            if check in dict1:
                dict1[check].append(i)
            else:
                dict1[check] = [i]
        return dict1.values()