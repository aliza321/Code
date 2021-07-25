class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in range(len(digits)):
            n += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(n+1)]
        
        