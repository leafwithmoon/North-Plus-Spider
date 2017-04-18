# -*- coding:utf-8 -*-
import os
import re
from bs4 import BeautifulSoup
from fetchPage import fetcher
from config import fid, fid_type, html_address

# init fetcher class
Crawler = fetcher()

# get max_pageNumber
res = Crawler.fetch('http://bbs.imoutolove.me/thread.php?fid-{0}-type-{1}.html '.format(fid, fid_type))
soup = BeautifulSoup(res.content, 'lxml')
max_pageNumber = int(soup.find_all(class_="pagesone")[0].text[9:13])

# get resource category and resource title
for pageNumber in range(1, max_pageNumber):
    res = Crawler.fetch('http://bbs.imoutolove.me/thread.php?fid-{0}-type-{1}-page-{2}.html'.format(fid, fid_type, pageNumber))
    soup = BeautifulSoup(res.content, 'lxml')
    for x in soup.find_all(class_='t_one')[5:-1]:
        the_psssword = []
        print x.find_all('td')[1].a.text, x.find_all('td')[1].h3.text, x.find_all('td')[1].h3.a.get('href')
        topic_res = Crawler.fetch(html_address + x.find_all('td')[1].h3.a.get('href'))
        topic_soup = BeautifulSoup(topic_res.content, 'lxml')
        for baiduyun_link in topic_soup.find_all(string=re.compile('pan.baidu.com/')):
            print "百度云", baiduyun_link.string
        for thunder_link in topic_soup.find_all(string=re.compile('magnet:\?xt=urn:btih:')):
            print "迅雷磁力", thunder_link.string
        for address in topic_soup.find_all(href=re.compile('http')):
            if re.findall(
                    '(bbs.imoutolove.me|bbs.north-plus.net|www.phpwind|slolita.taobao.com|masadora.net|imgbar.net|wpa.qq.com|plus.google.com|www.imagebam.com|soulxplus.net|.jpg|.png|.gif|.bmp)',
                    address.get('href')) == []:
                print "其他网盘", address.get('href')
            else:
                pass
        for password in topic_soup.find_all(string=re.compile(u'密码')):
            for p in re.compile('[A-Za-z0-9]+').findall(password):
                p.encode('utf-8')
                the_psssword.append(p)
            print password
        if the_psssword != []:
            print "密码：",the_psssword

        print "-------------------------------------------------------------------"

