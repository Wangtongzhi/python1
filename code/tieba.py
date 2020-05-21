import requests
class TieBa():
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url ="https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    def get_url_list(self):
        url_list = []
        for i in range(1000):
            url_list.append(self.url.format(i*50))
        return url_list
    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()
    def save_html(self,html_str,page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name,page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)
    def run(self):
        # 1构造url列表
        url_list=self.get_url_list()
        # 2遍历发送请求 获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            self.save_html(html_str,page_num)
        # 3保存
if __name__ == '__main__':
    tieba = TieBa("LOL")
    tieba.run()