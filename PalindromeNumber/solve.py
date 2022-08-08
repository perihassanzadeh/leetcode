class Solution:
    def isPalindrome(self, x: int) -> bool:
        xnew = str(x)
        loop = int(len(xnew)/2)
        
        for y in range(loop):
            if(xnew[y]!=xnew[-y-1]):
                return False
            
        return True