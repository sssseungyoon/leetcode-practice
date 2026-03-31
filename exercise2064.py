class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # O(n^2) approach
        target = sum(quantities) // n
        print("sum:",sum(quantities), "target:", target, "len:",len(quantities))
        print(quantities)
        if target == 0: return 1
        binary_search = False
        previous_jump = 1
        previously_visited_target = set()
        while True:
            print("previous jump", previous_jump)
            inter_mod = []
            inter = 0
            # make this into a O(1) time complexity
            for q in quantities:
                inter += q // target + (q % target > 0)
                if q % target > 0: inter_mod.append(q % target)
            print("total sum:", inter)
            print("inter mod:", inter_mod)
            if binary_search:
                previous_jump = 1 if previous_jump // 2 == 0 else previous_jump // 2
                if inter <= n:
                    if target in previously_visited_target: return target
                    previously_visited_target.add(target)
                    target -= previous_jump 
                else:
                    if target in previously_visited_target: return target - 1
                    previously_visited_target.add(target)
                    target += previous_jump
                print("new target", target)
            else:
                if inter <= n: 
                    return target
                else:
                    if min(inter_mod) > 1: binary_search = True
                    target += min(inter_mod)
                    previous_jump = min(inter_mod)
            print("")

# 

if __name__ == '__main__':
    sol = Solution()
    n = 19753
    quantities = [47466,40,60106,45058,87147,29906,131,22338,71535,89839,79891,15030,703,13417,322,78180,63622,67848,798,9,30251,24562,121,13760,73435,17227,214,25787,24191,41717,728,82290,208,18097,63790,79711,59398,59625,35575,93223,90741,97568,918,34063,10625,77167,26432,57239,28539,62532,389,803,569,771,271,85471,68211,66694,92715,95135,57179,37530,61263,65503,34180,47227]
    print(sol.minimizedMaximum(n,quantities))
