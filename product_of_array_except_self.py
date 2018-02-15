class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        left = 1
        for i in xrange(len(nums)):
            if i>0:
                left = left * nums[i - 1]
            result.append(left)
        right = 1
        for i in reversed(xrange(len(nums))):
            if i<(len(nums)-1):
                right = right * nums[i + 1]
            result[i] *= right
        return result