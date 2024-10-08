class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Edge case: if the grid is empty, return 0
        if not grid:
            return 0
        
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # A helper function to perform DFS and mark all connected land as visited
        def dfs(r, c):
            # If we are out of bounds or hit water ('W'), return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current landmass as visited by changing it to 'W'
            grid[r][c] = 'W'
            # Explore all four directions (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Initialize the count of islands
        island_count = 0
        
        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                # When we find land, we start a DFS and increase the island count
                if grid[r][c] == 'L':
                    dfs(r, c)
                    island_count += 1
        
        return island_count
