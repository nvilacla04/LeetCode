class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x 
        n = x/2

        while True:
            n_next = 0.5*(n + (x/n))
            if abs(n_next - n) < 0.005: 
                 break
            n = n_next
        return int(n_next) 
        #Nnext = 1/2(Xcurr + n/(Xcuur))