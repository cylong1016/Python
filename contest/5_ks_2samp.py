#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
������

����pythonʵ�ּ򻯰�˫����K-S���麯��
���룺

a,b�ֱ�Ϊ�ǿ�һά���飻ʾ������ : [1.0,2.0,3.0],[1.0,2.0,3.0]

�����

ks-valueΪ������KSֵ��ʾ����� : 0.0

ע�⣺

��1�����ܵ���math��scipy��numpy��
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