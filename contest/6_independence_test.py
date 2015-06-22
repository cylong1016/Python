#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
描述：

利用python实现简化版独立检验函数
输入：

A为二维数组，每行代表总体X的一个水平上的取值，每列代表总体Y的一个水平上的取值；示例输入 : [[1.0,2.0,3.0],[2.0,2.0,3.0]]

输出：

[c-val,p-value]分别代表检验结果C值与其对应的P值；示例输出 : [0.257937,0.879002]

注意：

（1）A中只有一行时，返回结果为[0.0, None]

（2）结果保留6位小数点

"""

from scipy import stats
import numpy

class Solution():
	def independence_test(self, A):
		if len(A) <= 1 or A == None:
			return [0.0, None]
		r = len(A)
		c = len(A[0])
		
		row = numpy.sum(A, 1)
		column = numpy.sum(A, 0)
		total = float(numpy.sum(A))
		
		x2 = 0.0
		for i in range(r):
			for j in range(c):
				Tij = column[j] * row[i] / total
				x2 += (A[i][j] - Tij) ** 2 / Tij
		
		p = stats.chi2.sf(abs(x2), (r - 1) * (c - 1))
		return [round(x2, 6), round(p, 6)]
		
s = Solution()
A = [[1.0, 2.0, 3.0], [2.0, 2.0, 3.0]]
print s.independence_test(A)