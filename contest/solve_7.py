#-*- coding:utf-8 -*-

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
			
