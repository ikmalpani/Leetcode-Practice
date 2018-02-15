class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        
        