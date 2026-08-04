from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        need_to_pass = [0] * numCourses
        graph = defaultdict(list)
        for course, prev_course in prerequisites:
            need_to_pass[course] += 1
            graph[prev_course].append(course)

        queue = deque()
        for course, courses_num in enumerate(need_to_pass):
            if courses_num == 0:
                queue.append(course)
        
        passed = set()
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            passed.add(course)
            for next_course in graph[course]:
                need_to_pass[next_course] -= 1
                if need_to_pass[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == numCourses else []