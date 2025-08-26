from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list) 
        in_degree = [0] * numCourses
        
        for courses, prereqs in prerequisites:
            graph[prereqs].append(courses)
            in_degree[courses] += 1
        print(graph)
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        return res if len(res) == numCourses else []

def main():
    numCourses = 4
    prerequisites = [[1,0], [2,0], [3,1], [3,2]]
    solution = Solution()
    result = solution.findOrder(numCourses, prerequisites)
    print(result)

if __name__ == "__main__":
    main()



