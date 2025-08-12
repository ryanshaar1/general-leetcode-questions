class Solution(object):
    def canJump(self, nums):
        index1 = 0
        index2 = 0
        if nums[0] == 0 and len(nums)==1:
            return True
        elif nums[0] == 0 and len(nums)>1:
            return False
        while index1>=0 and index1<len(nums)-1:
            if nums[index1]>0:
                index1+=1
            else:
                index2 = index1
                for i in range(index2):
                    index1-=1
                    if nums[index1]+index1>index2:
                        index1=index2+1
                        break
                if index1<index2:
                    return False
        return True
                    
        