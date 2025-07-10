class Solution(object):
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x1 - x0) * (y - y0) != (y1 - y0) * (x - x0):
                return False
        return True
