from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        sol = []

        def _generateParanthesis(open: int, closed: int):
            print("open:", open, "closed:", closed)
            if closed == 0:
                output.append("".join(sol))
                return
            if open > 0:
                sol.append("(")
                _generateParanthesis(open - 1, closed)
                sol.pop()
            if open < closed:
                sol.append(")")
                _generateParanthesis(open, closed - 1)
                sol.pop()

        _generateParanthesis(n, n)
        return output


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
