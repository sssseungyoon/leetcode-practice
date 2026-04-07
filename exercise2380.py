class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        s = s.lstrip("1").rstrip("0")
        print(s)
        for i in range(len(s)):
            if s[i] == "0" or (i < len(s) - 1 and s[i] == s[i + 1] == "1"):
                print(i)
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    s = "111000"
    print(sol.secondsToRemoveOccurrences(s))
