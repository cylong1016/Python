#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
������

����pythonʵ�ּ򻯰�Ƥ��ɭ���ϵ�����㺯��
���룺

x : һά���飻y : һά���飬��x��y������ͬ��ʾ������ : [1.0,2.0,3.0],[2.0,2.0,3.0]

�����

[r-val,p-value]�ֱ����Ƥ��ɭ���ϵ����������Pֵ��ʾ����� : [0.866025,0.333333]

ע�⣺

��1��scipy��ֻ��ʹ��scipy.x.ppf��scipy.x.sf����
	
��2��x,yΪ��ʱ������ֵΪ[None,None]

��3���������6λС����
"""

import math
from scipy import stats

class Solution():
	def pearsonr(self, x, y):
		if x is None or y is None or len(x) == 0:
			return [None, None]
		sx = math.sqrt(self.var(x) * len(x) / (len(x) - 1))
		sy = math.sqrt(self.var(y) * len(y) / (len(y) - 1))
		meanx = self.mean(x)
		meany = self.mean(y)
		rxy = 0.0
		for i in range(len(x)):
			rxy += ((x[i] - meanx) / sx) * ((y[i] - meany) / sy)
		rxy /= (len(x) - 1)
		if rxy == 1 or (len(x) - 2) == 0:
			return [1.0, 0.0]
		t = rxy * math.sqrt((len(x) - 2) / (1 - rxy ** 2))
		p_val = stats.t.sf(abs(t), len(x) - 2) * 2
		return [round(rxy, 6), round(p_val, 6)]
		
	def mean(self, arr):
		sumArr = 0.0
		for t in arr:
			sumArr += t
		mean = sumArr / len(arr)
		return mean

	def var(self, arr):
		mean = self.mean(arr)
		sumArr = 0.0
		for t in arr:
			sumArr += (t - mean) ** 2
		var = sumArr / len(arr)
		return var
		
s = Solution()
x = [1.0, 2.0, 3.0, 4.0]
y = [2.0, 2.0, 3.0, 5.0]
print stats.pearsonr(x, y)
print s.pearsonr(x, y)