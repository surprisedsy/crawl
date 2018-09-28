from bs4 import BeautifulSoup

html = '<td class="title black"><div class="tit3" id="t3" name="t3name">'\
        '<a href="/movie/bi/mi/basic.nhn?code=163533" title="안시성">안시성</a>'\
        '</div></td>'


# 1. Tag 조회
def ex1():

    bs = BeautifulSoup(html, "html.parser")

    tag = bs.td
    print(tag)

    tag = bs.div
    print(tag)

    print("==========")

    print(bs)
    print(bs.div)
    print(bs.div.a)


# 2. Attribute값 가져오기
def ex2():

    bs = BeautifulSoup(html, "html.parser")

    tag = bs.td
    print(tag["class"])

    tag = bs.div
    print(tag["id"])
    print(tag.attrs)


# 3. attrs로 조회
def ex3():

    bs = BeautifulSoup(html, "html.parser")

    tags = bs.find("td", attrs={"class" : "title"})
    print(tags)

    tags = bs.find(attrs={"title" : "안시성"})
    print(tags)

    tags = bs.find("a")
    print(tags)


if __name__ == "__main__" :

    #ex1()
    #ex2()
    ex3()








