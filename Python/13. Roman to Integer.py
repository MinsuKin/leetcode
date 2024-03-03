class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        res = 0
        i = 0
        while i < length:
            if i + 1 < length:
                if s[i] == 'I' and s[i + 1] == 'V':
                    res += 4
                    i += 2
                    continue
                elif s[i] == 'I' and s[i + 1] == 'X':
                    res += 9
                    i += 2
                    continue
                elif s[i] == 'X' and s[i + 1] == 'L':
                    res += 40
                    i += 2
                    continue
                elif s[i] == 'X' and s[i + 1] == 'C':
                    res += 90
                    i += 2
                    continue
                elif s[i] == 'C' and s[i + 1] == 'D':
                    res += 400
                    i += 2
                    continue
                elif s[i] == 'C' and s[i + 1] == 'M':
                    res += 900
                    i += 2
                    continue
            if s[i] == 'I':
                res += 1
                i += 1
            elif s[i] == 'V':
                res += 5
                i += 1
            elif s[i] == 'X':
                res += 10 
                i += 1               
            elif s[i] == 'L':
                res += 50
                i += 1
            elif s[i] == 'C':
                res += 100   
                i += 1             
            elif s[i] == 'D':
                res += 500  
                i += 1              
            elif s[i] == 'M':
                res += 1000  
                i += 1
        return res