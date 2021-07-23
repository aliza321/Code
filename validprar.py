class Solution:
    def isValid(self, s: str) -> bool:
        
        def is_Para(left, right):
            
            return left == '(' and right == ')' or left == '{' and right == '}' or left == '[' and right == ']'
        
        st = []
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            else:
                if not st or not is_Para(st[-1], ch):                
                    return False                    
                else:                
                    st.pop()
        
        return not st