# -*- coding:utf-8 -*-
import urllib2
import urllib
class urldownload:
    def __init__(self):
        pass

    def download(self,url):
        if url == None:
            return 
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        if response.getcode() == 200:
            content = response.read().decode('utf-8')
            return content
        else:
            return 
