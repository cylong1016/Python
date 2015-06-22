#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
描述：

利用python实现简化版皮尔森相关系数计算函数
输入：

x : 一维数组；y : 一维数组，且x、y长度相同；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]

输出：

[r-val,p-value]分别代表皮尔森相关系数、检验结果P值；示例输出 : [0.866025,0.333333]

注意：

（1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数

（2）x,y为空时，返回值为[None,None]

（3）结果保留6位小数点
"""

class Solution():
	def pearsonr(self, x, y):
		pass