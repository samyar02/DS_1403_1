import math
class Tower:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  
        self.left = 0 
        self.right = 0 
n = int(input()) 
output = []  # To store all the results
for _ in range(n):
    m = int(input()) 
    towers = []
    for i in range(m):
        a, b, c = map(int, input().split())
        towers.append(Tower(a, b, c))
    stack_left = []  # Stack to calculate leftsum
    stack_right = []  # Stack to calculate rightsum
    leftsum = 0
    rightsum = 0
    result = []
    for i in range(m):  # Single loop to calculate both left and right values
        # Update leftsum
        tower = towers[i]
        tower.left = leftsum
        while stack_left and stack_left[-1].a < tower.a:
            leftsum -= stack_left.pop().c
        stack_left.append(tower)
        leftsum += tower.c

        mirrored_index = m - 1 - i
        mirrored_tower = towers[mirrored_index]
        mirrored_tower.right = rightsum
        while stack_right and stack_right[-1].a < mirrored_tower.a:
            rightsum -= stack_right.pop().c
        stack_right.append(mirrored_tower)
        rightsum += mirrored_tower.c
    for i in range (m):    
        result.append(math.ceil(towers[i].b / (towers[i].left + towers[i].right)))

    output.append(" ".join(map(str, result)))  # Add the result of the current test case to the output

# Print all the results in one go for efficiency
print("\n".join(output))
