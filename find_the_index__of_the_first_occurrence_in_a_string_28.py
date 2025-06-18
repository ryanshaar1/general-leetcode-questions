class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        ls = haystack.split(needle)
        if len(ls)==1:
            return -1
        return len(ls[0])