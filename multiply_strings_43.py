class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = len(num1)
        n2 = len(num2)
        res = [0] * (n1 + n2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(n1):
            for j in range(n2):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                res[i + j] += digit1 * digit2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))
        