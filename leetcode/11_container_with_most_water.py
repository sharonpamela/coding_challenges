'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a 
container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented 
by array [1,8,6,2,5,4,8,3,7]. In this case, the max area 
of water (blue section) the container can contain is 49.
'''

def get_biggest_container(height):
    max_area_seen = float('-inf')
    l = 0
    r = len(height)-1
    while l < r:
        print(f"l: {l}, r: {r}")
        h = min(height[l], height[r])
        w = r - l
        area = h * w
        max_area_seen = max(max_area_seen, area)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return max_area_seen

height = [1,8,6,2,5,4,8,3,7]
height = [2,3,4,5,18,17,6]
print(get_biggest_container(height))


# Brute Force

'''
def get_biggest_container(height):
    max_area_seen = float('-inf')
    for i in range(len(height)):
        left_side = height[i]
        for j in range(i+1, len(height)):
            right_side = height[j]
            h = min(left_side, right_side)
            w = j - i
            max_area_seen = max(max_area_seen, h*w)
    return max_area_seen
'''