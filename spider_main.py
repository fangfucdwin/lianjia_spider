import html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):  # 初始化

        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, base_url ):

        try:
            page = 28
            count = 1
            for n in range(1, page + 1):
                craw_url = base_url.format(n)
                print('crawing Page%d ' % count)
                html_cont = self.downloader.download(craw_url )
                new_data = self.parser.parse(html_cont)
                self.outputer.collect_data(new_data)
                count += 1
        except Exception as e:
            print(str(e))
            # 根据报错信息提示错误

        #self.outputer.output_html()
        self.outputer.output_csv()



if __name__ == '__main__':

        base_url = "https://cd.fang.lianjia.com/loupan/nht1 pg{}"
        obj_spider = SpiderMain()
        obj_spider.craw(base_url)

