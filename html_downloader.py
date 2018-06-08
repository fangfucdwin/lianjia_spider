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
            'cookie': 'select_city=510100; lianjia_uuid=c4ecee09-c85b-43e5-aef7-d92bea55011a; gr_user_id=d265a8c7-4003-48d3-9d83-d46e5f23039f; _smt_uid=5b174e3e.198c8692; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1528254015; _jzqa=1.2321858760790652000.1528254015.1528254015.1528254015.1; _jzqc=1; _jzqy=1.1528254015.1528254015.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E6%88%90%E9%83%BD.-; _jzqckmp=1; gr_session_id_a1a50f141657a94e=4c534421-d742-42d4-9530-264c6c5134bc_true; UM_distinctid=163d309a553651-03e3ca0fd39872-7c103c49-1fa400-163d309a5555be; lianjia_token=2.0041a557bb39abeff450087e8aef6163e9; lianjia_ssid=43c3847c-1bca-4260-9217-bfb03cdaad51; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1528254081; _jzqb=1.4.10.1528254015.1; CNZZDATA1256144579=1395022583-1528250394-https%253A%252F%252Fcd.lianjia.com%252F%7C1528250394; CNZZDATA1255633284=800850075-1528253344-https%253A%252F%252Fcd.lianjia.com%252F%7C1528253344; CNZZDATA1255604082=989789178-1528253666-https%253A%252F%252Fcd.lianjia.com%252F%7C1528253666; _qzjc=1; _jzqa=1.2321858760790652000.1528254015.1528254015.1528254015.1; _jzqc=1; CNZZDATA1254525948=1142246318-1528248705-https%253A%252F%252Fcd.lianjia.com%252F%7C1528254105; _qzja=1.368752070.1528254084877.1528254084877.1528254084877.1528254472531.1528254479268.0.0.0.7.1; _qzjb=1.1528254084877.7.0.0.0; _qzjto=7.1.0; _jzqb=1.5.10.1528254015.1; lj_newh_session=eyJpdiI6InkzYU5Vc2ZHUWw1OHFJWWh2cXJPK1E9PSIsInZhbHVlIjoiTTc0cHJ5dEhcL21GVGFcL2NsdHZFQ0kwSTFZWHZ2SXJyZVFCbEYxSG9QODlyNVwvUnpGOVd5K0VcL2xsQnF6NXp3SGJcL0FJYk4wT0dFMHRjVGlrdUpLSjhnZz09IiwibWFjIjoiOGE4NTI0MDkzYTJlMzIxNjQyY2I5ZGM3ZGVmY2U0ZWRjZDI3Y2FhZTUxOTU5NWQwN2YxNGFiMzQ0ZDc0Y2UxYiJ9'
        }

        response = requests.get(url, headers=kv)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            return None

        return response.text