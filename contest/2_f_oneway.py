#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
描述：

利用python实现简化版单因素方差检验函数
输入：

sample1,sample2,... : 不定数量（至少一个）的一维数组；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]

输出：

[F-value, p-value]分别代表检验结果F值与其对应的P值；示例输出：[0.250000，0.643330]

注意：

（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数

（2）sample_i为空时，返回值为[None,None]

（3）结果保留6位小数点
"""

class Solution():
	def f_oneway(self, *args):
		pass