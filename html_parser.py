#-*- conding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser:
	def __init__(self):
        	pass
		
	def _get_new_url(self,content,url):
		new_urls = set()
		soup = BeautifulSoup(content)
		tags = soup.find_all('a',href= re.compile(r'^/item'))
		for link in tags:
			new_url = link['href']
			full_new_url = urlparse.urljoin(url,new_url)
			new_urls.add(full_new_url)
		return new_urls
		
	def _get_new_data(self,content):
		return content
		
	def parse(self,content,url):
		if content is None or url is None:
			return
		new_url = self._get_new_url(content,url)
		new_data = self._get_new_data(content)
		return new_url,new_data
