class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_match = bool(s) and (s[0] == p[0] or p[0] == '.')
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])


        
        
                    
                    
                
