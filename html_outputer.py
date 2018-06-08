import csv


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.extend(data)

    def output_html(self):
        fout = open('output_html.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<ul>")

        for data in self.datas:

            fout.write("<li>")

            fout.write('<h3>楼盘名称:<a href="%s" target="_blank">%s</a></h3>' % (data['block_url'],data['name']))
            fout.write("<b>楼盘所属区域:%s &nbsp&nbsp；</b>" % data['location'])
            fout.write("<b>单户面积:%s &nbsp&nbsp；</b>" % data['area'])
            fout.write("<b>价格:%s %s ；</b><br />" % (data['price'],data['desc']))

            fout.write("</li>")


        fout.write("</ul>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def output_csv(self):
        with open('output_csv.csv', 'w') as f:
            w = csv.writer(f)
            fieldnames = self.datas[0].keys()
            w.writerow(fieldnames)
            for data in self.datas:
                w.writerow(data.values())
