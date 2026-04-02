from typing import List


class Solution:
    # this will have O(n x k) time complexity
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        tracking: dict[int, tuple[int, bool]] = {
            i: (-(10**100), True) for i in range(k)
        }
        tracking[0] = (sum(nums[:k]), True)
        print(tracking)

        for i in range(k, len(nums)):
            index = (i + 1) % k
            new_chunk = sum(nums[(i + 1 - k) : (i + 1)])
            existing_chunk = tracking[index][0]
            print("new:", new_chunk, "existing:", existing_chunk, "i%k:", index)
            canMerge = tracking[index][1]
            if canMerge:
                localMax = max(existing_chunk, new_chunk, existing_chunk + new_chunk)
            else:
                localMax = max(existing_chunk, new_chunk)
            tracking[index] = (localMax, (localMax != existing_chunk))
            print("i:", i, "tracking:", tracking)

        output = -(10**100)
        for val, _ in tracking.values():
            if val > output:
                output = val
        return output


# instead of tracking the subtotal of each cases, which complicated the logic, I just use array slicing to calculate the subtotal
# failed to encompass the case where the local maximum doesn't correspond to the global maximum


if __name__ == "__main__":
    sol = Solution()
    nums = [-5, 1, 2, -3, 4]
    k = 2
    print(sol.maxSubarraySum(nums, k))
