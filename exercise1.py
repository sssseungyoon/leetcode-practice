class Solution:
    # two numbers that add up tot he target number; assume that there exists a unique solution;
    # assigning them in a hashmap -> O(n)
    # hashmap look up -> O(n)
    def solution(self, nums, target):
        dict = {}
        for (i,num) in enumerate(nums):
            # the sum of same number equals the target
            if target - num in dict:
                return [dict[target-num],i]
            if not num in dict:
                dict[num] = i 
        return []

if __name__ == '__main__':
    nums = [3,2]
    target = 6
    sol = Solution()
    print(sol.solution(nums, target))
    
