# -*- coding:utf-8 -*-
import url_manager
import url_download
import html_parser
import content_output
import os

class spardermain:
    def __init__(self):
        self.urlmanager = url_manager.UrlManager()
        self.urldownload = url_download.urldownload()
        self.htmlparser = html_parser.HtmlParser()
        self.contentoutput = content_output.ContentOutput()

    def start(self,url):
        self.urlmanager.add_new_url(url)
        while self.urlmanager.has_new_url():
       		url = self.urlmanager.pop_url()
		print '正在抓取：' 
		print url
            	html_content = self.urldownload.download(url)
            	new_urls,url_data = self.htmlparser.parse(html_content,url)
            	self.urlmanager.add_new_urls(new_urls)
            	self.contentoutput.collect(url_data)

        self.contentoutput.output()



if __name__ == '__main__':
    init_url = 'https://baike.baidu.com/item/百科'
    spider = spardermain()
    spider.start(init_url)
