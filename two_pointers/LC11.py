"""

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                if j > i:
                    area = min(h1, h2) * (j - i)
                    if area > max_area:
                        max_area = area
        return max_area
