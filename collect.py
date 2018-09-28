import time
from datetime import datetime

import pandas as pd
from itertools import count

from bs4 import BeautifulSoup
from selenium import webdriver

from collection.crawler import crawling

RESULT_DIRECTORY = "__result__"

def crawling_pelicana():

    results = []

    # for page in range(1, 2):
    for page in count(start=1):

        html = crawling("http://pelicana.co.kr/store/stroe_search.html?page={}&branch_name=&gu=&si=".format(page))

        bs = BeautifulSoup(html, "html.parser")
        tag_table = bs.find("table", attrs={"class" : "table mt20"})
        tag_tbody = tag_table.find("tbody")
        tags_tr = tag_tbody.findAll("tr")

        if(len(tags_tr) == 0):
            break

        for tag_tr in tags_tr:

            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            results.append((name, address))

    table = pd.DataFrame(results, columns=["name", "address"])
    table.to_csv("{0}/pelicana_table.csv".format(RESULT_DIRECTORY), encoding="utf-8", mode="w", index=True)



def crawling_nene():

    results = []

    # for page in range(1, 5):
    for page in count(start=1):

        html = crawling("https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A" % page)

        bs = BeautifulSoup(html, "html.parser")
        tags_div = bs.findAll("div", attrs={"class" : "shopInfo"})

        for tag_div in tags_div:

            name = tag_div.find("div", attrs={"class" : "shopName"}).text
            address = tag_div.find("div", attrs={"class" : "shopAdd"}).text
            results.append((name, address))

        if(len(tags_div) < 24):
            break

    table = pd.DataFrame(results, columns=["name", "address"])
    table.to_csv("{0}/nene_table.csv".format(RESULT_DIRECTORY), encoding="utf-8", mode="w", index=True)



def crawling_kyochon():

    results = []

    for sido1 in range(1, 18):
        for sido2 in count(start=1):

            url = ("http://www.kyochon.com/shop/domestic.asp?sido1={}&sido2={}&txtsearch=").format(sido1, sido2)
            html = crawling(url)

            if html is None:
                break

            bs = BeautifulSoup(html, "html.parser")
            tag_ul = bs.find("ul", attrs={"class" : "list"})

            for tag_a in tag_ul.findAll("a"):
                tag_dt = tag_a.find("dt")

                if tag_dt is None:
                    break

                name = tag_dt.get_text()
                address = tag_a.find("dd").get_text().strip().split("\r\n")[0]
                results.append((name, address))

    table = pd.DataFrame(results, columns=["name", "address"])
    table.to_csv("{0}/kyochon_table.csv".format(RESULT_DIRECTORY), encoding="utf-8", mode="w", index=True)



def crawling_goobne():

    url = "https://www.goobne.co.kr/store/search_store.jsp"

    wd = webdriver.Chrome("D:/Programming/04 PythonWeb/chromedriver_win32/chromedriver.exe")
    wd.get(url)
    time.sleep(3)

    results = []

    for page in count(start=1):

        # 1. JAVA Script 실행
        script = ("store.getList({})").format(page)
        wd.execute_script(script)
        print("{0} : success for request [{1}]".format(datetime.now(), script))
        time.sleep(3)

        # 2. JAVA Script 실행결과 HTML(Rendering된 HTML 가져오기)
        html = wd.page_source

        # 3. parsing with bs4
        bs = BeautifulSoup(html, "html.parser")
        tag_body = bs.find("tbody", attrs={"id" : "store_list"})
        tags_tr = tag_body.findAll("tr")

        # 4. 끝 검출
        if tags_tr[0].get("class") is None:
            break

        for tag_tr in tags_tr:

            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]

            results.append((name, address))

    table = pd.DataFrame(results, columns=["name", "address"])
    table.to_csv("{0}/goobne_table.scv".format(RESULT_DIRECTORY), encoding="utf-8", mode="w", index=True)



if(__name__ == "__main__"):

    crawling_pelicana()
    crawling_nene()
    crawling_kyochon()
    crawling_goobne()


