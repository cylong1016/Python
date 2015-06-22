__author__ = 'Li'

import urllib
from scipy import stats


class Solution:
	def solve(self):
		page = open('F:/data.txt')
		raw_data = page.read()
		page.close()

		data = eval(raw_data)['data']
		total = 0.0
		n = len(data)
		for row in data:
			prg_lenth = row[2]
			if prg_lenth >= 49 or prg_lenth <= 5 or 10 < prg_lenth <= 25:
				n -= 1
			else:
				if 5 < prg_lenth <= 10:
					prg_lenth *= 4.33
				total += prg_lenth

		mean = total / n
		sigma = 4.0
		zeta = stats.norm.isf(0.05 / 2)

		num = sigma / (n ** 0.5) * zeta

		upper = mean + num
		lower = mean - num

		return [round(lower, 6), round(upper, 6)]


print Solution().solve()