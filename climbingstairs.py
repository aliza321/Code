class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        pp= 1
        p = 2
        c = 0
        for s in range(3, n+1):
            c = pp + p
            pp = p
            p = c
        return c