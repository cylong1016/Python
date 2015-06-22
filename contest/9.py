from scipy import stats
import numpy


class Solution:
	def solve(self):
		page = open('F:/data.txt')
		raw_data = page.read()
		page.close()

		data = eval(raw_data)['data']

		A = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
		for row_data in data:
			prg_len = row_data[2]
			if not (prg_len <= 5 or 10 < prg_len <= 25 or prg_len >= 49):
				if 5 < prg_len <= 10:
					prg_len *= 4.33
				if row_data[5] == 1:
					i = 1
				else:
					i = 0
				if prg_len <= 37:
					j = 0
				elif prg_len >= 41:
					j = 1
				else:
					j = 2
				A[i][j] += 1

		row = numpy.sum(A, 1)
		column = numpy.sum(A, 0)
		n = float(numpy.sum(A))

		r = len(A)
		m = len(A[0])

		chi2 = 0.0
		for j in range(m):
			e1j = A[1][j]
			t1j = row[1] * column[j] / n
			chi2 += (e1j - t1j) ** 2 / t1j

		p = stats.chi2.sf(chi2, (r - 1) * (m - 1))
		return [chi2, p]

print Solution().solve()