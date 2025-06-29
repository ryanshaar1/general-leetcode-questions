class Solution(object):
    def maximumWealth(self, accounts):
            l = []

            for i in accounts:
                l.append(sum(i))
            return max(l)
        