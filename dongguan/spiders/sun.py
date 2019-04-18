# -*- coding: utf-8 -*-
import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
import re
from scrapy.linkextractors import  LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.spiders import Rule
#from scrapy_redis.spiders import RedisCrawlSpider
#from pyquery import PyQuery as pq
#from lxml import etree
from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    # redis_key = 'sunspider:start_urls'
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    link_list = LinkExtractor(allow=('page=\d+'))
    link_lis = LinkExtractor(allow=(r'http://wz.sun0769.com/html/question/\d+/\d+.shtml'))

    rules = [
        Rule(link_list, follow=True),
        Rule(link_lis,callback='parse_res',follow=True) ##回调函数加上引号
    ]


    def parse_res(self,response):
        # print(response.text)
        # item = DongguanItem()
        # doc = pq(etree.HTML(response.text))
        # text = doc('.p3 .tgray14').text()
        # item['question'] = re.search('提问：(.*?)编号',text).group(1)
        # item['content'] = doc('.c1').text()
        # item['status'] = doc('.text14_2 .cleft').text().split('：')[-1]
        # item['time'] = doc('.text14_2 .cright .te12h').text().split('：')[-1]

        item = DongguanItem()
        item['question'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()')[0].extract().strip().replace('\xa0', '')
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()')[0].extract().replace('\xa0', '')
        item['status'] = response.xpath('//div[@class="wzy3_1"]/span/text()')[0].extract().replace('\xa0', '')
        item['time'] = response.xpath('//div[@class="wzy3_2"]/span[1]/text()')[0].extract().replace('\xa0', '')

        yield item





