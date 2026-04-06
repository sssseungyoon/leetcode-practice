from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def _jump(n: int, counter: int):
            if n == 0:
                print("now returning")
                return counter

            if n not in memo:
                jumps = []
                for i in range(n):
                    distance = n - i
                    print("i:", i, "distance:", distance, "nums[i]:", nums[i])
                    if distance <= nums[i]:
                        print("true")
                        jumps.append(_jump(i, counter + 1))
                print("jumps:", jumps)
                memo[n] = min(jumps)
            return memo[n]

        return _jump(len(nums) - 1, 0)


if __name__ == "__main__":
    sol = Solution()
    nums = [
        5,
        6,
        4,
        4,
        6,
        9,
        4,
        4,
        7,
        4,
        4,
        8,
        2,
        6,
        8,
        1,
        5,
        9,
        6,
        5,
        2,
        7,
        9,
        7,
        9,
        6,
        9,
        4,
        1,
        6,
        8,
        8,
        4,
        4,
        2,
        0,
        3,
        8,
        5,
    ]
    print(sol.jump(nums))
