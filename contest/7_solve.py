#-*- coding:utf-8 -*-
# 2015-06-20
# author cylong

"""
描述：

蒙特卡罗方法，或称计算机随机模拟方法，是一种基于随机数的计算方法，在金融工程学，宏观经济学，计算物理学等领域应用广泛。
试编写函数solve(a,b)，利用蒙特卡罗方法计算函数f(x)=(e^(-x2/2))/√2√π在区间[a,b]上的定积分并返回，其中b>a>0。

输入：

a,b分别为正浮点数

输出：

m: 定积分值

注意：

（1）为保证精确性，蒙特卡罗模拟次数至少为100000

（2）不能使用scipy.integrate库
"""

import math
import random

class Solution:
	def solve(self, a, b):
		if ((a == None) or (b == None) or (a >= b)):
			return 0
		count = 880000
		incount = 0.0
		maxY = self.f(a)
		area = (b - a) * maxY 
		for i in range(count):
			x = random.uniform(a, b)
			y = random.uniform(0, maxY)
			if y < self.f(x):
				incount += 1
		return float(incount) / count * area

	def f(self, x):
		return (math.exp(-x ** 2 / 2.0)) / math.sqrt(2 * math.pi)

s = Solution()
print s.solve(1, 5)
			
