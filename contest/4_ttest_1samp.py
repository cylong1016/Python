#-*- coding:utf-8 -*-

"""
描述：

利用python实现简化版单总体T检验函数
输入：

a : 非空一维数组；popmean：假设总体期望值；示例输入 : [1.0,2.0,3.0],2.0

输出：

[t-val,p-value]分别代表检验结果T值与其对应的P值；示例输出 : [0.000000,1.000000]

注意：

（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数

（2）结果保留6位小数点
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