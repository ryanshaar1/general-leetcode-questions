class Solution(object):
    def lemonadeChange(self, bills):
        num5 = 0
        num10 = 0
        num20 = 0

        for i in bills:
            if i == 5:
                num5+=1
            elif i == 10:
                if num5<1:
                    return False
                num10+=1
                num5-=1
            else: 
                if num10 >= 1 and num5 >= 1:
                    num10 -= 1
                    num5 -= 1
                elif num5 >= 3:
                    num5 -= 3
                else:
                    return False
        return True
        