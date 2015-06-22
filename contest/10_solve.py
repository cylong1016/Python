#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
描述：

仍然利用NSFG数据（url为http://112.124.1.3:8060/getData/101.json），验证母亲年龄Y对婴儿出生体重W是否有影响。假设W=a+bY， 试写函数solve利用最小二乘法拟合a,b的值，并且计算其测定系数r2
输入：

调查样本数据，格式为{data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}

输出：

[a,b,r2]
"""

import urllib
import json

class Solution:
	def solve(self):
		url = "http://112.124.1.3:8060/getData/101.json"
		page = urllib.urlopen(url)
		html = page.read()
		
		data = json.loads(html)['data']
		n = len(data)
		sumX = 0.0
		sumY = 0.0
		lxy = 0.0
		lxx = 0.0
		for r in data:
			agepreg = r[6]
			totalwgt_oz = r[4]
			sumX += agepreg
			sumY += totalwgt_oz
			lxy += totalwgt_oz * agepreg
			lxx += agepreg ** 2
		meanX = sumX / n
		meanY = sumY / n
		lxy -= sumX * sumY / n
		lxx -= sumX ** 2 / n
		b = lxy / lxx
		a = meanY - b * meanX
		
		
		SR = 0.0
		ST = 0.0
		for r in data:
			SR += (b * r[6] + a - meanY) ** 2
			ST += (r[4] - meanY) ** 2
		r2 = SR / ST
		
		return [a, b, r2]

s = Solution()
print s.solve()