#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
������

����pythonʵ�ּ򻯰浥���ط�����麯��
���룺

sample1,sample2,... : ��������������һ������һά���飻ʾ������ : [1.0,2.0,3.0],[2.0,2.0,3.0]

�����

[F-value, p-value]�ֱ���������Fֵ�����Ӧ��Pֵ��ʾ�������[0.250000��0.643330]

ע�⣺

��1��scipy��ֻ��ʹ��scipy.x.ppf��scipy.x.sf����

��2��sample_iΪ��ʱ������ֵΪ[None,None]

��3���������6λС����
"""
from scipy import stats

class Solution():
	def f_oneway(self, *args):
		if not len(args):
			return [None, None]
		sum = 0.0
		n = 0.0
		QT = 0.0
		QA = 0.0
		for arr in args:
			if not len(arr):
				return [None, None]
			sumAi = 0.0
			for i in arr:
				sum += i
				n += 1
				QT += i ** 2
				sumAi += i
			QA += sumAi ** 2 / len(arr)
		C = sum ** 2 / n
		ST = QT - C
		SA = QA - C
		Se = ST - SA
		fT = n - 1
		fA = len(args) - 1
		fe = n - len(args)
		f_val = SA / fA / (Se / fe)
		p_val = stats.f.sf(f_val, fA, fe)
		return [round(f_val, 6), round(p_val, 6)]
		
s = Solution()
print s.f_oneway([1.0, 2.0, 3.0],[2.0, 2.0, 3.0], [3.0, 4.0, 5.0])