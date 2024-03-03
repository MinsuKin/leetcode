class Solution:
    
    def turnback(self, grid: List[List[str]], x: int, y: int, height: int, width: int):
 
        if y+1 < width and x < height:
            if grid[x][y+1] == "1":
                grid[x][y+1] = "-1"
                self.turnback(grid, x, y+1, height, width)

        if y < width and x+1 < height:
            if grid[x+1][y] == "1":
                grid[x+1][y] = "-1"
                self.turnback(grid, x+1, y, height, width)
                
        if y-1 >= 0:        
            if y-1 < width and x < height:
                if grid[x][y-1] == "1":
                    grid[x][y-1] = "-1"
                    self.turnback(grid, x, y-1, height, width)
        
        if x-1 >= 0:
            if y < width and x-1 < height:
                if grid[x-1][y] == "1":
                    grid[x-1][y] = "-1"
                    self.turnback(grid, x-1, y, height, width)

    def numIslands(self, grid: List[List[str]]) -> int:
        x = 0
        y = 0
        cnt = 0
        
        height = len(grid)
        width = len(grid[0])

        for x in range(height):
            for y in range(width):
                if grid[x][y] == "1":
                    cnt += 1
                    grid[x][y] = "-1"
                    self.turnback(grid, x, y, height, width)
                    
        return cnt

# neetcode
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
        
#         islands = 0
#         q = collections.deque()
#         visit = set()
#         rows, cols = len(grid), len(grid[0])
        
#         def dfs(r, c):
#             if (r not in range(rows) or
#                 c not in range(cols) or
#                 grid[r][c] == "0" or
#                 (r, c) in visit):
#                 return
            
#             visit.add((r, c))
#             directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc)
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     islands += 1
#                     dfs(r, c)
#         return islands