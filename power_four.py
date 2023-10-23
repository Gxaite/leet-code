'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while (x<n):
            x = 4 * x
                
        if x == n:return True
        else:return False