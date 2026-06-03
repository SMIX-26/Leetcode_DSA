class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in result:
                return [result[complement], i]

            result[nums[i]] = i
