#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
������

����pythonʵ�ּ򻯰�������麯��
���룺

AΪ��ά���飬ÿ�д�������X��һ��ˮƽ�ϵ�ȡֵ��ÿ�д�������Y��һ��ˮƽ�ϵ�ȡֵ��ʾ������ : [[1.0,2.0,3.0],[2.0,2.0,3.0]]

�����

[c-val,p-value]�ֱ���������Cֵ�����Ӧ��Pֵ��ʾ����� : [0.257937,0.879002]

ע�⣺

��1��A��ֻ��һ��ʱ�����ؽ��Ϊ[0.0, None]

��2���������6λС����

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