from typing import List


class Solution:
    # this will have O(n x k) time complexity
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        tracking: dict[int, int] = {}
        maximum = 0
        for i in range(k):
            print("sum:", sum(nums[i:k]))
            tracking[i] = sum(nums[i:k])
            maximum += nums[i]
        nums = nums[k:]
        print("maximum:", maximum, "nums:", nums, "tracking", tracking)

        skip = set()
        for i, num in enumerate(nums):
            # update the nums
            for start, subtotal in tracking.items():
                if start in skip:
                    continue
                subtotal += num
                tracking[start] = subtotal
                print("num:", num, "start:", start, "subtotal:", subtotal)
                if (i - start + 1) % k == 0:
                    if subtotal > maximum:
                        maximum = subtotal
                    if subtotal <= 0 and i + 1 < len(nums):
                        print("skip")
                        # you can't delete an item from the dict ig
                        skip.add(start)
                        # i am gues
                        tracking[i + 1] = nums[i + 1]
                print(tracking)

        return maximum


if __name__ == "__main__":
    sol = Solution()
    nums = [-5, 1, 2, -3, 4]
    k = 2
    print(sol.maxSubarraySum(nums, k))
