#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
描述：

利用python实现简化版双样本K-S检验函数
输入：

a,b分别为非空一维数组；示例输入 : [1.0,2.0,3.0],[1.0,2.0,3.0]

输出：

ks-value为检验结果KS值；示例输出 : 0.0

注意：

（1）不能调用math、scipy、numpy包
"""

class Solution():
	def ks_2samp(self, data1, data2):
		data = data1 + data2
		data.sort()
		D = 0.0
		for tmp in data:
			num_1 = 0.0
			for t in data1:
				if t <= tmp:
					num_1 += 1.0
			num_2 = 0.0
			for t in data2:
				if t <= tmp:
					num_2 += 1.0
			a = abs(num_1 / len(data1) - num_2 / len(data2))
			D = max(a, D)
		return round(D, 6)
		

s = Solution()
data1 = [1, 1.3, 2, 3.4]
data2 = [1, 2.1, 3.1]
print s.ks_2samp(data1, data2)