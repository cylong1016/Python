#-*- coding:utf-8 -*-

class Solution:
    def solve(self, A):
        if(len(A) <= 1):
            return A
        b = []
        c = []
        num = A[0]
        for i in A[1:]:
            if i < num:
                b.append(i)
            else:
                c.append(i)
        return self.solve(b) + [num] + self.solve(c)
		
s = Solution()
A = [3, 2, 10, 8, 4, 16]
print s.solve(A)