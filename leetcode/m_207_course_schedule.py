import re


def canFinish(numCourses, prerequisites):
        
    # add all of the prereqs into a dict
    prs = { i:[] for i in range(numCourses) }
    for c, pre in prerequisites:
        prs[c].append(pre)
      
    visitedCourses = set()
    def dfs(course):
        if course in visitedCourses: return False
        if prs[course] == []: return True

        visitedCourses.add(course)
        for pre in prs[course]:
            # if the dfs returns false for a single course
            # then we can return false early
            if not dfs(pre): return False

        # remove the visited prerequisites from current course
        prs[course] = []
        visitedCourses.remove(course)
        return True
        
    for course in range(numCourses):
        if not dfs(course): return False
    return True





numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))