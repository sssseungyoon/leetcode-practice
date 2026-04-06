from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        print(len(nums))
        # greedy approach
        start = 1
        end = nums[0] + 1
        jump = 0
        if sum(nums) == 0 or len(nums) == 1:
            return 0
        while end < len(nums):
            for i in range(start, end):
                if i + nums[i] >= end:
                    start, end = i + 1, i + nums[i] + 1
            jump += 1

        return jump + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 1, 4]
    print(sol.jump(nums))
