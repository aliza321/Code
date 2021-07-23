class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        r = 0
        while n>0:
            re = n %10
            n = (n - re)//10
            r= r*10+re
        return x == r
        