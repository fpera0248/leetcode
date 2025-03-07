class Solution:
    
    def countCollisions(self, directions: str) -> int:
        total, colls = len(directions), 0
        if total == 1:return 0

        left, rite = 0, total - 1
        while left < total and directions[left] == "L":
            left += 1
        while 0 < rite and directions[rite] == "R":
            rite -= 1
        for curr in directions[left: rite + 1]:
            if curr == "S":continue
            colls += 1
    
        return colls
