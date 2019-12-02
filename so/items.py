# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = Field()
	votes = Field()
	question = Field()
	accepted_answer = Field()
	tags = Field()
	link = Field()
	pass
