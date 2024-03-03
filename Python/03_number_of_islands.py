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
