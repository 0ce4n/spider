# -*- coding:utf-8 -*-

class urlmanager:
    def __init__(self):
        self.new_url_list = set()
        self.old_url_list = set()

    def add_new_url(self, url):
        if url == None:
            return 
        if url != None and url not in self.new_url_list and url not in self.old_url_list:
            self.new_url_list.add(url)
    
    def add_new_urls(self, urls):
        if urls == None or len(urls) == 0:
            return 
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_url_list) != 0

    def pop_url(self):
        if len(self.new_url_list) == 0:
            return 
        url = self.new_url_list.pop()
        self.old_url_list.add(url)
        return url