class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Initialize queue with all rotten oranges and count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # If no fresh oranges, no time needed
        if fresh == 0:
            return 0
        
        minutes = -1  # BFS level counter
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Multi-source BFS
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Rot adjacent fresh orange
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        
        # If any fresh orange remains → impossible
        return minutes if fresh == 0 else -1