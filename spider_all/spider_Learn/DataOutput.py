import codecs


class DataOutput:
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<th>名词链接</th>")
        fout.write("<th>百科名词</th>")
        fout.write("<th>百科释义</th>")
        fout.write("</tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td align='left'>%s</td>" %data['url'])
            fout.write("<td align='left'>%s</td>" %data['title'])
            fout.write("<td align='left'>%s</td>" %data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()


