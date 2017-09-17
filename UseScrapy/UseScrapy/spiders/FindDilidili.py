# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from UseScrapy.items import DilidiliItem


class FinddilidiliSpider(CrawlSpider):
    name = 'FindDilidili'
    allowed_domains = ['www.dilidili.wang', 'bbs.005.tv']
    start_urls = ['http://www.dilidili.wang/hougong/']
# http://www.dilidili.wang/hougong/

    rules = (
        Rule(LinkExtractor(allow=r'dilidili'), follow=True),
        Rule(LinkExtractor(allow=r'/anime/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'bbs.005.tv/'), callback='parse_item_bbs')
    )

    def parse_item(self, response):
        print("deal with dilidili")
        i = DilidiliItem()
        name_css = 'div.detail>dl>dd>h1::text'
        url_css = 'li.list_xz>a[href*="pan"]::attr(href)'
        i['name'] = response.css(name_css).extract()
        # i['url'] = response.css(url_css).extract()
        i['url'] = response.css(url_css).extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print(i['name'])
        print(i['url'])
        if i['url'] == []:
            print("no url")
            return None
        return i

    def parse_item_bbs(self, response):
        print("deal with bbs")
        i = DilidiliItem()
        name_css = 'span#thread_subject::text'
        url_css = 'td.t_f>a[href*="pan"]::attr(href)'
        i['name'] = response.css(name_css).extract()
        # i['url'] = response.css(url_css).extract()
        i['url'] = response.css(url_css).extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print(i['name'])
        print(i['url'])
        return i
