from bs4 import BeautifulSoup as BS
import requests
import json
from model import Course


class Parser:
    def urls_and_check(self, message):
        urls = ['https://coursive.id/api/v1/courses/chto-takoe-vlog-i-kak-ego-vesti/',
                'https://coursive.id/api/v1/courses/chto-takoe-podkast-i-kak-ego-zapisyvat/',
                'https://coursive.id/api/v1/courses/kak-pisat-stati-kotorye-podnimayut-vazhnye-ru',
                'https://coursive.id/api/v1/courses/chto-takoe-kontent-i-kak-ego-sozdavat',
                'https://coursive.id/api/v1/courses/chto-takoe-gendernoe-ravenstvo',
                'https://coursive.id/api/v1/courses/feminizm-zhonundo-kurs'
                ]
        return self.parser(urls[message - 1])

    def parser(self, url):
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')
        soup2 = json.loads(soup.text)
        title1 = soup2['title']
        blocks = soup2['blocks']
        list1 = []
        list1.append(title1)
        for i in blocks:
            list1.append(i['title'])
        if not Course.table_exists():
            Course.create_table()
        Course.create(
            name=list1[0],
            title=list1[1:]
        )
        return list1



