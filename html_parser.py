import re
import json
from bs4 import BeautifulSoup
from lxml import etree


class HtmlParser(object):

    def _get_new_data(self, block_datas):
        block_data_list = []
        datas = block_datas.find_all("div", class_='resblock-desc-wrapper')
        for data in datas:
            block_data_dic = {}
            name = data.find('a', class_="name").string
            sale_status = data.find('span', class_="sale-status").string
            location = data.find('div', class_="resblock-location").find('span').string
            area = data.find('div', class_="resblock-area").find('span').string
            price = data.find('span', class_="number").string
            if data.find('span', class_="desc") != None:
                desc = data.find('span', class_="desc").string.replace('\xa0', '')
            else:
                desc = '无该数据'
            url = data.find('a', class_="name")['href']
            block_data_dic['name'] = name
            block_data_dic['sale_status'] = sale_status
            block_data_dic['location'] = location
            if area == None:
                block_data_dic['area'] = '无该数据'
            else:
                block_data_dic['area'] = area
            block_data_dic['price'] = price
            block_data_dic['desc'] = desc
            block_data_dic['block_url'] = 'https://cd.fang.lianjia.com' + url
            block_data_list.append(block_data_dic)

        return block_data_list

    def parse(self, html_cont):
        if html_cont is None:
            return
        block_datas = BeautifulSoup(html_cont, 'html.parser')
        new_data = self._get_new_data(block_datas)
        return new_data


