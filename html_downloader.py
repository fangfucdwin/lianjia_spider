import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        kv = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
            'host': 'cd.fang.lianjia.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': '登陆信息cookie'
        }

        response = requests.get(url, headers=kv)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            return None

        return response.text
