#-*- coding:utf-8 -*-

"""
������

����pythonʵ�ּ򻯰浥����T���麯��
���룺

a : �ǿ�һά���飻popmean��������������ֵ��ʾ������ : [1.0,2.0,3.0],2.0

�����

[t-val,p-value]�ֱ���������Tֵ�����Ӧ��Pֵ��ʾ����� : [0.000000,1.000000]

ע�⣺

��1��scipy��ֻ��ʹ��scipy.x.ppf��scipy.x.sf����

��2���������6λС����
"""
import math
import numpy
from scipy import stats

class Solution():
	def ttest_1samp(self, a, popmean):
		mean = self.mean(a)
		var = self.var(a) * len(a) / (len(a) - 1)
		s = math.sqrt(var)
		t_val = (mean - popmean) / (s / math.sqrt(len(a)))
		p_val = stats.t.sf(numpy.abs(t_val), len(a) - 1) * 2
		# p_val = 2 * stats.norm.sf(numpy.abs(t_val))
		return [round(t_val, 6), round(p_val, 6)]
		
	def mean(self, arr):
		sumArr = 0.0
		for tmp in arr:
			sumArr += tmp
		mean = sumArr / len(arr)
		return mean

	def var(self, arr):
		mean = self.mean(arr)
		sumArr = 0.0
		for tmp in arr:
			sumArr += (tmp - mean) ** 2
		var = sumArr / len(arr)
		return var
		
s = Solution()
a = [1.0, 2.0, 3.0, 5]
print s.ttest_1samp(a, 2.0)