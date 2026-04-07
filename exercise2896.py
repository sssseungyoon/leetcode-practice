class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        # if the # of 0's/1's differ by an odd number, then it is impossible, as the # of 0's and 1's contained in one string can only be switched by an even number in the case of 00 and 11.
        # tactic, use the first operation as much as you can

        # create an array consisted of the indices at which the two arrays differ, it will be a sorted array
        # find the diff in length
        # if the length is odd -> termiante; if the length is 0, the move to the last step; if the length is even, then apply the last step within the array
        # I am having trouble in formulating an algorithm that would find the minimum number of replacements, as there are multiple possibilites to keep track of
        # this dyanmic programming shit is getting me

        extracted = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                extracted.append(i)

        # case when the conversion is impossible
        if len(extracted) % 2 != 0:
            return -1

        print(extracted)

        memo = {}

        def DP(i: int):
            if i < 0:
                return 0
            elif i == 0:
                return x / 2
            if i not in memo:
                memo[i] = min(
                    DP(i - 1) + x / 2, DP(i - 2) + (extracted[i] - extracted[i - 1])
                )
                print("at i:", i, memo[i])
            return memo[i]

        return int(DP(len(extracted) - 1))


if __name__ == "__main__":
    sol = Solution()
    s1 = "1100011000"
    s2 = "0101001010"
    x = 2
    print(sol.minOperations(s1, s2, x))
