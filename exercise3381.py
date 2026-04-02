from typing import List


class Solution:
    # now it is O(n) time complexity
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        max_vals = [-(10**100)] * k
        tracking_vals = [0] * k
        max_vals[0], tracking_vals[0] = (
            sum(nums[:k]),
            (sum(nums[:k]) if sum(nums[:k]) >= 0 else 0),
        )

        tracking: dict[int, tuple[int, int]] = {i: (-(10**100), 0) for i in range(k)}
        # tuple (maximum, tracking, canMerge)
        tracking[0] = (sum(nums[:k]), sum(nums[:k]) if sum(nums[:k]) >= 0 else 0)
        print(tracking)

        new_chunk = sum(nums[:k])
        for i in range(k, len(nums)):
            index = (i + 1) % k
            new_chunk += (
                nums[i] - nums[i - k]
            )  # using this instead of array slicing allows to reduces the time complexity of this operation to constant time
            print("new chunk:", new_chunk)
            existing_chunk = tracking_vals[index]
            merged_chunk = new_chunk + existing_chunk
            print("new:", new_chunk, "existing:", existing_chunk, "i%k:", index)
            # case when the existing chunk is greater than the current max
            max_val = max_vals[index]
            if merged_chunk > max_val:
                max_val = merged_chunk
            # merge when the subtotal is greater than 0 else reset
            merged_chunk = merged_chunk if merged_chunk >= 0 else 0
            max_vals[index], tracking_vals[index] = max_val, merged_chunk
            print("i:", i, "tracking:", tracking)
        return max(max_vals)
        output = -(10**100)
        for val, _ in tracking.values():
            if val > output:
                output = val
        return output

    """
    how to reduce the overhead?
    1. Use list, which can directly access the value over dictionary which involves hash operations
    2. Modulo is expensive as it involves division. Use a counter that resets to improve the time complexity
    3. Tuple unpacking and repacking is expensive, use two separate lists for this operation
    """


if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -1]
    k = 1
    print(sol.maxSubarraySum(nums, k))
