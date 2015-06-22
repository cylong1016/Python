#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
描述：

仍然利用NSFG数据（url为http://112.124.1.3:8060/getData/101.json），
但这次我们想验证第一胎婴儿是否更倾向于更早或更晚出生而较少准时出生的假设，因此需要利用卡方检验计算出其卡方值chisq及推翻假设的p值。
试写函数solve计算卡方值chisq及p值
输入：

调查样本数据，格式为{"data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}

输出：

[chisq,p]

注意：

（1）婴儿第几周出生数据由于被调查人选填错误等原因出现了一些不合理数据，比如错填了月份（5<prglength<=10），其他错填（prglength<=5, 
10<prglength<=25, prglength>=49），对于错填月份的情况，将月份*4.33作为其周数，对于其他错填情况则舍弃此条数据

（2）一般认为，如果婴儿在第37周或更早出生，那就是提前出生；准时出生则是在第38周到第40周；而延后出生则是在41周或更晚
"""

import urllib
from scipy import stats
import json
import numpy

class Solution:
	def solve(self):
		url = "http://112.124.1.3:8060/getData/101.json"
		page = urllib.urlopen(url)
		html = page.read()
		
		data = json.loads(html)['data']
		A = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
		for r in data:
			prglength = r[2]
			if not (prglength <= 5 or 10 < prglength <= 25 or prglength >= 49):
				if 5 < prglength <= 10:
					prglength *= 4.33
				if r[5] == 1:
					i = 1
				else:
					i = 0
				if prglength <= 37:
					j = 0
				elif prglength >= 41:
					j = 1
				else:
					j = 2
				A[i][j] += 1

		row = numpy.sum(A, 1)
		column = numpy.sum(A, 0)
		total = float(numpy.sum(A))
		
		r = len(A)
		c = len(A[0])
		
		x2 = 0.0
		for j in range(c): # 只计算第一行
			T1j = column[j] * row[1] / total
			x2 += (A[1][j] - T1j) ** 2 / T1j
		
		p = stats.chi2.sf(abs(x2), (r - 1) * (c - 1))
		return x2, p
		
s = Solution()
print s.solve()