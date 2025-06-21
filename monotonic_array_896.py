class Solution(object):
    def isMonotonic(self, nums):
        if nums == sorted(nums) or nums[::-1] ==sorted(nums):
            return True
        return False
        