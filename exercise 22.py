from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def _generateParanthesis(open: int, closed: int, prev: str) -> List[str]:
            print("open:", open, "closed:", closed, "prev:", prev)
            if closed == 0:
                return [prev]
            if open <= 0:
                return _generateParanthesis(open, closed - 1, prev + ")")
            if open < closed:
                return _generateParanthesis(
                    open - 1, closed, prev + "("
                ) + _generateParanthesis(open, closed - 1, prev + ")")
            else:
                return _generateParanthesis(open - 1, closed, prev + "(")

        return _generateParanthesis(n, n, "")


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
