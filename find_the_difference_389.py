class Solution(object):
    def findTheDifference(self, s, t):
        for i in range(len(s)):
            t = t.replace(s[i],"",1)
        return t
        