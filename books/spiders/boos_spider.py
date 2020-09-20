# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BooksItem


class BoosSpiderSpider(scrapy.Spider):
    name = 'books_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_css='li.col-xs-6')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.book_parse)

        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url  
            yield scrapy.Request(next_url, callback=self.parse)


    def book_parse(self,response):
        book = BooksItem()
        sel = response.css('div.col-sm-6.product_main')
        book['name'] = sel.xpath('h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['stock'] = sel.css('p.instock').re_first('In stock \((\d+)') 
        book['rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating (.+)')

        yield book
        
