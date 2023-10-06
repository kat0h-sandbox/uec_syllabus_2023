import requests
import time
from bs4 import BeautifulSoup

headers = {
        "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
}

def get_all_class():
    url = "http://kyoumu.office.uec.ac.jp/syllabus/2023/GakkiIchiran_31_0.html"
    response = requests.get(url=url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")
    sp = soup.select("body > table:nth-of-type(2)")[0].select("table")[5].select("tr")[1:]

    print("A")
    ls = []
    f = open('list', 'w')
    for i in sp:
        ls2 = []
        classcode = get_class_code(
            "http://kyoumu.office.uec.ac.jp/syllabus/2023/" + i.find('a').get('href')
        )
        for j in i.find_all("td"):
            ls2.append(j.get_text())
        ls2.append(classcode)
        ls.append(ls2)
        print(ls2, file=f)
        print(ls2)
        time.sleep(0.5)
    f.close()

    

def get_class_code(url):
    response = requests.get(url=url, headers=headers)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")
    sp = soup.find_all("th")

    for i, x in enumerate(sp):
        if i == 2:
            tr = x.find_parent('tr')
            td = tr.find('td')
            code = td.get_text()
            return code


get_all_class()
