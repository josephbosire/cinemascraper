# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    poster = scrapy.Field()
    duration = scrapy.Field()
    schedule =scrapy.Field()
    cinema = scrapy.Field()
    show_date = scrapy.Field()
    show_times = scrapy.Field()

