import math

class Tower:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  
        self.left = 0 
        self.right = 0 

n = int(input()) 
output = []  

for _ in range(n):
    m = int(input()) 
    towers = []
    stack = []
    leftsum = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        tower = Tower(a, b, c)
        tower.left = leftsum
        while stack and stack[-1].a < tower.a:
            leftsum -= stack.pop().c
        stack.append(tower)
        leftsum += tower.c
        towers.append(tower)

    stack = [] 
    righsum = 0
    result = []
    for i in range(m - 1, -1, -1):
        tower = towers[i]
        tower.right = righsum
        while stack and stack[-1].a < tower.a:
            righsum -= stack.pop().c
        stack.append(tower)
        righsum += tower.c
        result.append(math.ceil(tower.b / (tower.left + tower.right)))
    output.append(" ".join(map(str, result[::-1])))
print("\n".join(output))
