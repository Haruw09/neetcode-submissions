from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_prerequisites = defaultdict(list)
        for course, needed_course in prerequisites:
            courses_prerequisites[course].append(needed_course)

        status = [0] * numCourses
        def can_pass(course: int) -> bool:
            if status[course] == 1:
                return False
            if status[course] == 2:
                return True

            status[course] = 1
            for needed_course in courses_prerequisites[course]:
                if not can_pass(needed_course):
                    return False

            status[course] = 2
            return True

        return all(can_pass(i) for i in range(numCourses))
            