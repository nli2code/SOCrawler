import scrapy
import json
from scrapy import Spider
from scrapy.selector import Selector
from so.items import SoItem

class SoSpider(scrapy.Spider):
	name = 'so'
	main_url = 'https://stackoverflow.com'

	def __init__(self):
		with open('user_config.json') as f:
			config = json.load(f)
		self.tag = config['tag']
		self.pagenum = config['pagenum']
		self.pagesize = config['pagesize']

	def start_requests(self):
		urls = []
		for i in range(1, self.pagenum):
			url = self.main_url + '/questions/tagged/' + self.tag + '?page=' + str(i) + '&sort=votes&pagesize=' + str(self.pagesize)
			urls.append(url)
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for post in Selector(response).xpath('//div[@class="summary"]/h3'):
			post_url = post.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
			post_url = self.main_url + post_url
			yield scrapy.Request(url = post_url, callback=self.parse_each)
	
	def parse_each(self, response):
		item = SoItem()
		item['title'] = response.css('h1 a::text').extract()[0]
		item['question'] = response.css('.question .post-text').extract()[0]
		item['tags'] = response.css('.question .post-tag::text').extract()
		ac_div = response.xpath('//div[@class="answer accepted-answer"]').css('.post-text').extract()
		if ac_div == None:
			item['accepted_answer'] = ''
		else:
			item['accepted_answer'] = ac_div
		item['link'] = response.url
		yield item
