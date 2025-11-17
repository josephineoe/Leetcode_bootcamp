class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Build graph + indegree count
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Queue of courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            # Reduce indegree of children
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                # If indegree becomes 0 → available to take
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we could take all courses, return order
        return order if len(order) == numCourses else []