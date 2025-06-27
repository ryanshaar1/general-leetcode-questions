class Solution(object):
    def isRobotBounded(self, instructions):
        directions = ["north", "east", "south", "west"]
        current = 0  

        position = {
            "north": 0,
            "east": 0,
            "west": 0,
            "south": 0
        }

        for i in instructions:
            if i == 'G':
                position[directions[current]] += 1
            elif i == "R":
                current = (current + 1) % 4
            elif i == "L":
                current = (current - 1) % 4

        if position["north"] == position["south"] and position["east"] == position["west"]:
            return True


        if current != 0:
            return True

        return False
