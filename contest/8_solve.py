#-*- coding:utf-8 -*-
# 2015-06-22
# author cylong

"""
������

��������������Ԥ�����ģ�CDC����1973�꿪ʼ����ȫ����ͥ�ɳ����飨NSFG����Ŀ�����ռ�������������ͥ���������״�������������к���Ů������Ϣ����
���д�2002��1�µ�3���ռ��ĵ������ݣ�urlΪhttp://112.124.1.3:8060/getData/101.json���������������������ݣ�ÿ�����ݰ��� caseid����ʶ����,
 prglength��Ӥ���ڼ��ܳ�����, outcome�����н����1��ʾ�����, totalwgt_oz��Ӥ��������������λ��˾��, birthord���ڼ�̥,1��ʾ��һ̥��,
 agepreg������ʱ���䣩, finalwgt���������ߵ�ͳ��Ȩ�أ������������������������Ⱥ���������˿��еı�������������Ⱥ��Ȩ��ƫ�ͣ�����Ϣ
���ĳ�о���ʾ��Ӥ�������������Ϸ���Ϊ16����̬�ֲ�����д����solve����Ӥ��ƽ�������������������䣨����ˮƽΪ95%����
���룺

�����������ݣ���ʽΪ{data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}

�����

[lower,upper]�ֱ����ƽ�����������Ĺ�������������

ע�⣺

��1��Ӥ���ڼ��ܳ����������ڱ�������ѡ������ԭ�������һЩ���������ݣ�����������·ݣ�5<prglength<=10�����������prglength<=5,
 10<prglength<=25, prglength>=49�������ڴ����·ݵ���������·�*4.33��Ϊ�������������������������������������
"""

import urllib
from scipy import stats
import json

class Solution:
	def solve(self):
		url = "http://112.124.1.3:8060/getData/101.json"
		page = urllib.urlopen(url)
		html = page.read()
		
		data = json.loads(html)['data']
		total_prg_len = 0.0
		n = 0
		for r in data:
			prglength = r[2]
			if prglength <= 5 or 10 < prglength <= 25 or prglength >= 49:
				continue;
			n += 1
			if 5 < prglength <= 10:
				prglength *= 4.33
			total_prg_len += prglength
			
		mean_pre = total_prg_len / n
		sigma = 4.0
		za = stats.norm.isf(0.05 / 2)
		tmp = sigma * za / (n ** 0.5)
		lower = mean_pre - tmp
		upper = mean_pre + tmp
		return [round(lower, 6), round(upper, 6)]
		
s = Solution()
print s.solve()