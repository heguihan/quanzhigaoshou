#coding:utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')





# http://www.booktxt.net/5_5907/
# http://www.booktxt.net/5_5907/2208631.html

class quanzhigaoshou(BaseSpider):
	name = 'quanzhigaoshou'
	allowed_domains = ['booktxt.net']
	start_urls = ['http://www.booktxt.net/5_5907/']
	chapt = 0
	test = []


	def parse(self, response):
		hxp = Selector(response)

		titles = hxp.select("//*[@id='list']/dl/dd/a/text()").extract()[9:]
		urls = hxp.select("//*[@id='list']/dl/dd/a/@href").extract()[9:]
		self.test = titles

		domain = 'http://www.booktxt.net/'

		for urlaa in urls:
			url = domain + urlaa
			# self.title = titles[i]
			yield Request(url, callback=self.parse_txt)


	def parse_txt(self, response):
		self.chapt += 1
		print '***************************************'
		print 'chapt = ' + str(self.chapt)
		# with open('fir.html', 'wb') as f:
		# 	f.write(response.body)

		hxp = Selector(response)
		content = hxp.select("//*[@id='content']/text()").extract()
		# //*[@id="wrapper"]/div[4]/div/div[2]/h1
		titles = hxp.select('//*[@id="wrapper"]/div[@class="content_read"]//div[@class="bookname"]/h1/text()').extract()





		name = self.chapt / 100
		print ' name = '+ str(name)
		filrname = '第' + str(name+1) + '部分'+ '.txt'
		with open(filrname, 'a') as f:
			f.write('*\n')
			f.write('**\n')
			f.write('***\n')
			f.write('****\n')
			f.write('*****\n')
			f.write('******\n')
			f.write('*******\n')
			f.write('********\n')
			f.write('*********\n')
			f.write('**********\n')
			f.write(self.test[self.chapt-1])
			f.write('\n')	
			f.write('**********\n')
			f.write('*********\n')
			f.write('********\n')
			f.write('*******\n')
			f.write('******\n')
			f.write('*****\n')
			f.write('****\n')
			f.write('***\n')
			f.write('**\n')
			f.write('*\n')
			f.write('\n\n\n\n')
			for ss in content:

				f.write(ss)



