class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(s) == 0 and len(t) == 0:
            return True
        count = {}
        for key in s:
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
        for key in t:
            if key in count:
                count[key] -= 1
            else:
                count[key] = -1
        changes = 0
        for each in count.values():
            changes += abs(each)
        changes = changes/2
        if changes == 0:
            return True
        else: return False
        