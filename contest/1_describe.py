#-*- coding:utf-8 -*-

"""
描述：

利用python实现简化版描述函数
输入：

a : 一维数组

输出：

[mean,var,skew,kurt]分别代表均值、方差、偏度、峰度

注意：

（1）不能调用math、scipy、numpy包

（2）为了使正态分布峰度为0，此处对峰度值做减3处理
"""

class Solution():
	def describe(self, arr):
		if len(arr) == 1:
			var = None
		else:
			var = self.var(arr) * len(arr) / (len(arr) - 1)
			var = round(var, 6)
		mean = round(self.mean(arr), 6)
		skew = round(self.skew(arr), 6)
		kurt = round(self.kurt(arr), 6)
		
		return [mean, var, skew, kurt]
	
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

	def skew(self, arr):
		mean = self.mean(arr)
		var = self.var(arr)
		if var == 0.0:
			return 0.0
		sumArr = 0.0
		for t in arr:
			sumArr += (t - mean) ** 3
		skew = sumArr / len(arr) / (var ** 1.5)
		return skew

	def kurt(self, arr):
		mean = self.mean(arr)
		var = self.var(arr)
		if var == 0:
			return -3.0
		sumArr = 0.0
		for t in arr:
			sumArr += (t - mean) ** 4
		kurt = sumArr / len(arr) / (var ** 2) - 3.0
		return kurt
		
s = Solution()
arr = [1]
print s.describe(arr)
arr = [1, 1, 1, 1]
print s.describe(arr)
arr = [4, 3, 2, 1]
print s.describe(arr)
arr = [4, 3, 2, 1, 1]
print s.describe(arr)
