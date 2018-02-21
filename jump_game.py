class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_reach = 0
        for i, x in enumerate(nums):
            if max_reach < i:
                return False
            if max_reach >= n - 1:
                return True
            max_reach = max(max_reach, i + x)