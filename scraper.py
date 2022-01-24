#!/usr/bin/env python3
from requests_html import HTMLSession

class Scraper():
    def scrapdata(self, tag):
       url = f'https://quotes.toscrape.com/tag/{tag}'
       #initialize a session
       #this allows us ti use session pbjects to scrap data
       s = HTMLSession()
       r = s.get(url)
       print(r.status_code)
       #returns list of quotes data in the page
       quotes = r.html.find('div.quote')
       q_list = []
       for quote in quotes:
           item = {
                "text" : quote.find('span.text', first=True).text.strip(),
                "author" : quote.find('small.author', first=True).text.strip()
           }
           q_list.append(item)
       return q_list


q = Scraper()
q.scrapdata('life')
