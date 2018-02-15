class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for each in nums:
            if each in dict.keys():
                dict[each] += 1
            else:
                dict[each] = 1
        return sorted(dict, key=dict.get, reverse=True)[:k]