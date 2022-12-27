class Solution:
    def removeStars(self, s: str) -> str:
        '''
        first solution
        its take long time and memory usage
        '''
        """
        
        a = list(s)
        b= a.copy()
        for val in b:
            if val == '*':
                a.pop(a.index(val) - 1)
                a.remove(val)
                b= a.copy()
        return "".join(a)"""
        
        #---------------------------------
        '''
        second solution
        '''
        
        s3 = ''
        for char in s:
            if char == '*':
                s3 = s3[:-1]
            else:
                s3 += char

        return s3
