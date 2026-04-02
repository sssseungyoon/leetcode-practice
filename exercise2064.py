from typing import List

# tried implementing a heurstic that would effectively increment the counter. Upon reaching the condition for the first time, the algorithm would then perform a bianry search. However, this approach over-complicates the logic. Instead, I will try making the outer loop into a binary search instead of sticking with an iterative loop.


class Solution:
    def calculateInter(self, quantities: List[int], target: int) -> int:
        inter = 0
        for q in quantities:
            inter += q // target + (q % target > 0)
        return inter

    def _minimizedMaximum(self, n: int, quantities: List[int], lo: int, hi: int) -> int:
        mid = (lo + hi) // 2
        print("low:", lo, "mid:", mid, "hi:", hi)
        # terminating condition
        # left-leaning case
        if mid == lo:
            if self.calculateInter(quantities, hi) <= n:
                return lo
            return hi
        inter = self.calculateInter(quantities, mid)

        if inter > n:
            return self._minimizedMaximum(n, quantities, mid, hi)
        else:
            return self._minimizedMaximum(n, quantities, lo, mid)

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo = 1
        hi = max(quantities)
        if n >= sum(quantities):
            return 1
        return self._minimizedMaximum(n, quantities, lo, hi)

    def minimizedMaximumIterativeApproachON2(
        self, n: int, quantities: List[int]
    ) -> int:
        target = sum(quantities) // n
        if target == 0:
            return 1
        while True:
            inter = 0
            for q in quantities:
                inter += q // target + (q % target > 0)

            print("inter", inter)
            if inter <= n:
                return target
            else:
                print("target:", target)
                target += 1


if __name__ == "__main__":
    sol = Solution()
    n = 75729
    quantities = [
        34213,
        59196,
        27754,
        613,
        25291,
        45324,
        154,
        69367,
        61811,
        34,
        91027,
        21373,
        29834,
        36,
        56079,
        73771,
        713,
        364,
        36040,
        14155,
        96823,
        18947,
        13618,
        28852,
        55857,
        66453,
        96567,
        12864,
        30360,
        895,
        73537,
        721,
        86379,
        94911,
        15833,
        96621,
        24411,
        17805,
        22049,
        23296,
        12565,
        58815,
        962,
        76760,
        12662,
        163,
        68312,
        14070,
        60367,
        78622,
        66,
        43709,
        97948,
        90163,
        36111,
        47201,
        30201,
        17722,
        655,
        17727,
        70926,
        40273,
        56442,
        84342,
        894,
        58547,
        79618,
        29839,
        24798,
        981,
        40984,
        32775,
        85520,
    ]
    print(
        "binary:",
        sol.minimizedMaximum(n, quantities),
        "iterative:",
        sol.minimizedMaximumIterativeApproachON2(n, quantities),
    )
