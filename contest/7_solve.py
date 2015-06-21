#-*- coding:utf-8 -*-
# 2015-06-20
# author cylong

"""
������

���ؿ��޷�������Ƽ�������ģ�ⷽ������һ�ֻ���������ļ��㷽�����ڽ��ڹ���ѧ����۾���ѧ����������ѧ������Ӧ�ù㷺��
�Ա�д����solve(a,b)���������ؿ��޷������㺯��f(x)=(e^(-x2/2))/��2�̦�������[a,b]�ϵĶ����ֲ����أ�����b>a>0��

���룺

a,b�ֱ�Ϊ��������

�����

m: ������ֵ

ע�⣺

��1��Ϊ��֤��ȷ�ԣ����ؿ���ģ���������Ϊ100000

��2������ʹ��scipy.integrate��
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
			
