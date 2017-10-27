# -*- coding: utf-8 -*-
import scrapy
from movies.items import MovieItem

class IncinemasSpider(scrapy.Spider):
    name = 'incinemas'
    allowed_domains = ['kenyabuzz.com']
    start_urls = ['https://www.kenyabuzz.com/movies/']

    def parse(self, response):
        for movie in response.css('div.movie'):
            movie_item = MovieItem()
            movie_item['title'] = movie.css('a.movie__title::text').extract()
            movie_item['poster'] = movie.css('img.movie-list').xpath('@src').extract()
            movie_item['duration'] = movie.css('p.movie__time::text').extract()[0]
            locations = []
            for location_times in movie.css("div.time-select__group"):
                movie_item['cinema'] = location_times.css('p.time-select__place').css("a::text").extract()
                movie_item['show_date'] = location_times.css("h6::text").extract()
                movie_item['show_times'] = [link.css("a::text").extract()[0].replace("\r","").replace("\n","").replace("\t","").replace(" ","") for link in location_times.css('a.time-select__item2')]
                yield movie_item
