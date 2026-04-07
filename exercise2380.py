class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        zeros = 0
        for c in s:
            if c == "0":
                zeros += 1
            elif zeros > 0:
                seconds = max(seconds + 1, zeros)
        return seconds


if __name__ == "__main__":
    sol = Solution()
    s = "111000"
    print(sol.secondsToRemoveOccurrences(s))
