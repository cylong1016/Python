import urllib


class Solution:
	def solve(self):
		page = urllib.urlopen('http://112.124.1.3:8060/getData/101.json')
		#page = open('F:/data.txt')
		raw_data = page.read()
		page.close()

		data = eval(raw_data)['data']
		data2 = []
		for row in data:
			data2.append([row[6], row[4]])

		n = len(data2)

		x_sum = 0.0
		y_sum = 0.0
		lxx = 0.0
		lxy = 0.0
		for row in data2:
			x_sum += row[0]
			y_sum += row[1]
			lxx += row[0] ** 2
			lxy += row[0] * row[1]

		x_mean = x_sum / n
		y_mean = y_sum / n
		lxx -= x_sum ** 2 / n
		lxy -= x_sum * y_sum / n

		b = lxy / lxx
		a = y_mean - b * x_mean

		sr = 0.0
		st = 0.0
		for row in data2:
			sr += (row[0] * b + a - y_mean) ** 2
			st += (row[1] - y_mean) ** 2
		r2 = sr / st

		return [a, b, r2]

print Solution().solve()