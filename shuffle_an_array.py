from random import shuffle

class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums
        
    def shuffle(self):
        shuffled_array = self.nums[:] 
        shuffle(shuffled_array)
        return shuffled_array