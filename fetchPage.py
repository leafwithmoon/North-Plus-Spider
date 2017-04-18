import requests
from config import username, password

class fetcher:
    def __init__(self):
        self.s = requests.Session()
        self.login()

    def login(self):
        data = {
            'jumpurl': 'http://bbs.imoutolove.me',
            'step': 2,
            'lgt': 0,
            'pwuser': username,
            'pwpwd': password,
            'hideid': 0,
            'cktime': '3153600'
        }
        res = self.s.post("http://bbs.imoutolove.me/login.php?", data=data)
        return res.status_code

    def search(self, keyWord):
        data = {
            'keyword': keyWord,
            'step': 2,
            'method': 'OR',
            'pwuser': '',
            'sch_area': 0,
            'f_fid': 'all',
            'sch_time': 'all',
            'orderway': 'postdate',
            'asc': 'DESC'
        }
        res = self.s.post("http://bbs.imoutolove.me/search.php", data=data)
        return res

    def fetch(self, url):
        res = self.s.get(url)
        return res