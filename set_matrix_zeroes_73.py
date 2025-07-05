class Solution(object):
    def setZeroes(self, matrix):
        l = []

        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0:
                    l.append([i,j])
        

        for index in l:
            for i in range(len(matrix[index[0]])):
                matrix[index[0]][i] = 0
            for i in range(len(matrix)):
                matrix[i][index[1]] = 0
        

        