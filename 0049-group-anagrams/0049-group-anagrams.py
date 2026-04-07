from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        ans = defaultdict(list)
        
        for i in strs:
            key = [0]*26
            for c in i:
                key[ord(c)-ord('a')]+=1
            key = tuple(key)
            ans[key].append(i)
        return ans.values()
