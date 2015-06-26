#-*- coding:utf-8 -*-
# 2015-06-22
# author lwp

class Solution():
	def ks_2samp(self, data1, data2):
		total_max = max(max(data1), max(data2))
		total_min = min(min(data1), min(data2))

		n1 = len(data1)
		n2 = len(data2)

		n = max(n1, n2)

		step = float(total_max - total_min) / n

		max_delta = 0
		upper = total_min
		for i in range(n):
			upper += step
			count1 = 0
			for x in data1:
				if x <= upper:
					count1 += 1
			count2 = 0
			for x in data2:
				if x <= upper:
					count2 += 1
			delta = abs(float(count1) / n1 - float(count2) / n2)
			max_delta = max(max_delta, delta)

		return max_delta


print Solution().ks_2samp([1, 1.3, 2, 3.4], [1, 2.1, 3.1])