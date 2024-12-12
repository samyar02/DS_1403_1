import math
class Tower:
    def __init__(self, a, b, c):
        self.a = a  # Height of the tower
        self.b = b  # Resistance of the tower
        self.c = c  # Power of the tower
        self.left = 0  # Cumulative power from left
        self.right = 0  # Cumulative power from right

def find_left(towers, i, b):
    """
    Find the left value of the first tower j (where j < i)
    such that tower[j].a >= tower[i].a.
    """
    for j in range(i - 1, -1, -1):  # Look at all previous towers
        if towers[j].a >= b:
            return towers[j].left
    return 0  # Return 0 if no such tower is found

def find_right(towers, i, m):
    """
    Find the right value of the first tower j (where j > i)
    such that tower[j].a >= tower[i].a.
    """
    for j in range(i + 1, m):  # Look at all subsequent towers
        if towers[j].a >= towers[i].a:
            return towers[j].right
    return 0  # Return 0 if no such tower is found


n = int(input())  # Number of scenarios
for _ in range(n):
    m = int(input())  # Number of towers in the scenario
    towers = []
    buff = 0
    preA = 0

    # Calculate the `left` values
    for i in range(m):
        line = input()
        values = list(map(int, line.split()))
        tower = Tower(*values)
        if preA >= tower.a:
            buff += tower.c 
        else:
            buff = tower.c + find_left(towers, i, tower.a)
        tower.left = buff
        preA = tower.a
        towers.append(tower)

    buff = 0
    preA = 0
    result = [] 
    for i in range(m - 1, -1, -1):
        tower = towers[i]
        if preA >= tower.a:
            buff += tower.c
        else:
            buff = tower.c + find_right(towers, i, m)
        tower.right = buff
        preA = tower.a
        left_val = towers[i - 1].left if i > 0 else 0  
        right_val = towers[i + 1].right if i < m - 1 else 0 
        result.append(math.ceil( tower.b / (left_val + right_val)))

    print(" ".join(map(str, result[::-1])))
