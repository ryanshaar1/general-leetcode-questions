class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        if len(arr)<2:
            return True
        s = sorted(arr)
        diff = s[0] -s[1]
        for i in range(len(s)-1):
            if s[i] - s[i+1] != diff:
                return False
        return True



        