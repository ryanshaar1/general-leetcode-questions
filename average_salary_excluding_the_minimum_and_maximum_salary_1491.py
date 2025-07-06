class Solution(object):
    def average(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))
        return round(float(sum(salary)) / len(salary), 5)
