class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # if you have an equal number of x's and z's use z
        # if you have more x's, then depending on the z'
        return 2 * min(x, y) + (abs(x - y) > 0) + z
