# python 3.7
# author Eric

import requests
import time, random
import re

class NovelSpider():
    def __init__(self):
        self.session = requests.session() # download mechine
    
    def get_novel(self, url):
        '''download novel'''
        # download html of leader page of novel
        index_html = self.download(url, encoding='gbk')
        
        # get novel title
        title = re.findall(r'"article_title">(.*?)<', index_html)[0]

        # extract chapter information and url
        novel_chapter_infos = self.get_chapter_info(index_html)

        # create a file - <novel name>.txt
        fb = open('%s.txt' % title, 'w', encoding='utf-8')

        # download chapter
        for chapter_info in novel_chapter_infos:
            # wirte chapter title
            fb.write('%s\n' % chapter_info[1])
            # download chapter
            content = self.get_chapter_content(chapter_info[0])
            fb.write(content)
            fb.write('\n')
            print(chapter_info)
        fb.close()
        

    def download(self, url, encoding):
        '''download source code of html'''
        User_Agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",\
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",\
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",\
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",\
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",\
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"]
        time.sleep(random.random()*3)
        headers = {
            "User-Agent": random.choice(User_Agent),
            }
        response = self.session.get(url, headers=headers)
        response.encoding = encoding
        html = response.text
        return html

    def get_chapter_info(self, index_html):
        '''get the inforamtion of chapter'''
        div = re.findall(r'<DIV class="clearfix dirconone">.*?</DIV>', index_html, re.S)[0]
        info = re.findall(r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>', div)
        return info

    def get_chapter_content(self, chapter_url):
        '''download chapter content'''
        content = ''
        chapter_html = self.download(chapter_url, encoding='gbk')
        if chapter_html != '' and chapter_html != None:
            content = re.findall(r'<script type="text/javascript">style5\(\);</script>(.*?)<script', chapter_html, re.S)[0]

            # filter content
            content = content.replace('&nbsp;', '')
            content = content.replace('&quot;', '')
            content = content.replace('<br />', '')

            # replace enter
            content = content.replace('\r\n', '')

        return content


if __name__ == '__main__':
    novel_url = 'http://www.quanshuwang.com/book/69/69968'
    spider = NovelSpider()
    spider.get_novel(novel_url)