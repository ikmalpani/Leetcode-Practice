class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for each in nums:
            if each == 0:
                red += 1
            elif each == 1:
                white += 1
            elif each == 2:
                blue +=1
        nums[:red] = [0] * red
        nums[red:red+white] = [1] * white
        nums[red+white:] = [2] * blue
        print nums