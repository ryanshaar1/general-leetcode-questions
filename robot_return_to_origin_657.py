class Solution(object):
    def judgeCircle(self, moves):
        ud = 0
        lr = 0

        for i in range(len(moves)):
            if moves[i] == "U":
                ud += 1
            elif moves[i] == "D":
                ud -= 1
            elif moves[i] == "R":
                lr +=1
            elif moves[i] == "L":
                lr -=1
        return ud==lr==0
        