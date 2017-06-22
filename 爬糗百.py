#Author:xubojoy
# import HTMLParser
def getPage(url):
    '''url:目标网址URL
    return：HTML文档'''
    import urllib.request as urlreq
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/51.0.2704.103 Safari/537.36'}
    req = urlreq.Request(url,headers=headers)
    html = urlreq.urlopen(req).read()
    return html

print(getPage('http://www.qiushibaike.com'))

def qiushi01(page):
    '''传入解析得到的html文档，输出段子在一个字典中，包括作者和段子内容'''
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page,"xml")
    allCnt = soup.find_all('div',attrs={'class':'article block untagged mb15'})     #一页中所有段子
    for cnt in allCnt:
        author = cnt.h2.text  #作者
        content = cnt.find('div',attrs={'class':'content'}).text    #段子正文
        yield {'author':author,'content':content}


# print(list(qiushi01(getPage('http://www.qiushibaike.com'))))