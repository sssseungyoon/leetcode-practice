from typing import List


class Solution:
    # this will have O(n x k) time complexity
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        tracking: dict[int, tuple[int, int]] = {i: (-(10**100), 0) for i in range(k)}
        # tuple (maximum, tracking, canMerge)
        tracking[0] = (sum(nums[:k]), sum(nums[:k]) if sum(nums[:k]) >= 0 else 0)
        print(tracking)

        for i in range(k, len(nums)):
            index = (i + 1) % k
            new_chunk = sum(nums[(i + 1 - k) : (i + 1)])
            existing_chunk = tracking[index][1]
            merged_chunk = new_chunk + existing_chunk
            print("new:", new_chunk, "existing:", existing_chunk, "i%k:", index)
            # case when the existing chunk is greater than the current max
            max_val = tracking[index][0]
            if merged_chunk > max_val:
                max_val = merged_chunk
            # merge when the subtotal is greater than 0 else reset
            merged_chunk = merged_chunk if merged_chunk >= 0 else 0
            tracking[index] = (max_val, merged_chunk)
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
    nums = [-10, -1]
    k = 1
    print(sol.maxSubarraySum(nums, k))
