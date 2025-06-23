class Solution(object):
    def calPoints(self, operations):
        score = []

        for i in operations:
            if i.lstrip('-').isdigit():              
                score.append(int(i))
            elif i == "C":
                score.pop()
            elif i == "D":
                score.append(score[-1]*2)
            else:
                score.append(score[-1] + score[-2])
        return sum(score)
        