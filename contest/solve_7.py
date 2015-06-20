#-*- coding:utf-8 -*-

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

# from math import e
import math
import random

class Solution:
	def solve(self,a,b):
		count = 100000
		incount = 0
		maxY = self.f(b)
		for i in range(count):
			x = random.uniform(a, b)
			y = random.uniform(0, maxY)
			if y <= self.f(x):
				incount += 1.0
		return incount / count

	def f(self, x):
		return (math.e ** (-x ** 2 / 2)) / ((2 ** 0.5) * ( math.pi** 0.5))

s = Solution()
print s.solve(2, 5)
			
