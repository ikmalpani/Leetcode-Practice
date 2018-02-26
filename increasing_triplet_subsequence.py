import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        i = nums[0]
        j = sys.maxint
        for each in nums:
            if each <= i:
                i = each
            elif each <= j:
                j = each
            else:
                return True
        return False