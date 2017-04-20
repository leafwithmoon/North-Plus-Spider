# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
from fetchPage import fetcher
from config import fid, fid_type, html_address, db, fid_table

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

        # init topic information
        topic = {}
        title = x.find_all('td')[1].h3.text
        url = x.find_all('td')[1].h3.a.get('href')
        category = fid_table.get(fid)
        baiduyun_link = []
        thunder_link = []
        other_link = []
        the_psssword = []
        possible_password = []
        print title, url

        # get every topic resource
        topic_res = Crawler.fetch(html_address + url)
        topic_soup = BeautifulSoup(topic_res.content, 'lxml')

        # get all baiduYun link
        for link in topic_soup.find_all(href=re.compile('http://pan.baidu.com/')):
            print "百度云", link.get('href')
            baiduyun_link.append(link.string)

        # get all thunder link
        for link in topic_soup.find_all(string=re.compile('magnet:\?xt=urn:btih:')):
            print "迅雷磁力", link.string
            thunder_link.append(link.string)

        # get all other link like CC pan and others
        for link in topic_soup.find_all(href=re.compile('http')):
            if re.findall(
                    '(pan.baidu.com|bbs.imoutolove.me|bbs.north-plus.net|www.phpwind|slolita.taobao.com|masadora.net|imgbar.net|wpa.qq.com|plus.google.com|www.imagebam.com|soulxplus.net|.jpg|.png|.gif|.bmp)',
                    link.get('href')) == []:
                print "其他网盘", link.get('href')
                other_link.append(link.get('href'))
            else:
                pass

        # get all password and store possible password in a list
        for password in topic_soup.find_all(string=re.compile(u'密码')):
            for p in re.compile('[A-Za-z0-9 ]+').findall(password):
                p.encode('utf-8')
                the_psssword.append(p)
            print password
            possible_password.append(password)

        # complete the topic information
        topic["title"] = title
        topic["url"] = url
        topic["category"] = category
        topic["baiduyun_link"] = baiduyun_link if baiduyun_link != [] else False
        topic["thunder_link"] = thunder_link if thunder_link != [] else False
        topic["other_link"] = other_link if other_link != [] else False
        topic["the_password"] = the_psssword if the_psssword != [] else False
        topic["possible_password"] = possible_password if possible_password != [] else False

        # insert the topic into database
        new_topic = topic.copy()
        result = db.topic.insert(new_topic)
        if not result:
            print "insert error at {0} {1}".format(title, url)

        print "-------------------------------------------------------------------"

