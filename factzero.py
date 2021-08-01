class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = 1
        for i in range(2, n + 1):
             f *= i
        zc = 0
        while f % 10 == 0:
            zc += 1
            f //= 10
        return zc
        