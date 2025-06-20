class Solution(object):
    def plusOne(self, digits):
        i = -1
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        while abs(i) <= len(digits) and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if abs(i) > len(digits):  
            return [1] + digits
        digits[i] += 1
        return digits
