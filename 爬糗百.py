#Author:xubojoy
# import HTMLParser
def getPage(url):
    '''url:目标网址URL
    return：HTML文档'''
    import urllib.request
    import ssl
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/51.0.2704.103 Safari/537.36'}
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0')
    # req = urlreq.Request(url,headers=headers)
    ssl._create_default_https_context = ssl._create_unverified_context
    html = urllib.request.urlopen(req).read()
    return html

# print(getPage('http://www.budejie.com'))

def qiushi01(page):
    '''传入解析得到的html文档，输出段子在一个字典中，包括作者和段子内容'''
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page,"lxml")
    allCnt = soup.find_all('div',attrs={'class':'article block untagged mb15'})     #一页中所有段子
    for cnt in allCnt:
        # author = cnt.h2.text  #作者
        content = cnt.find('div',attrs={'class':'content'}).text    #段子正文
        yield content
        # yield {'author':author,'content':content}

if __name__ == '__main__':
    contentlist = list(qiushi01(getPage('http://www.qiushibaike.com')))
    for item in contentlist:
        print(item)



# import urllib.request
# import gzip
# from bs4 import BeautifulSoup
# url='http://news.sina.com.cn/c/nd/2017-02-05/doc-ifyafcyw0237672.shtml'
# req = urllib.request.Request(url)
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0')
# page = urllib.request.urlopen(req) # 模仿浏览器登录
# txt = page.read()
# # txt=gzip.decompress(txt).decode('utf-8')
# soup = BeautifulSoup(txt, 'lxml')
# title = soup.select('#artibodyTitle')[0].text
# print(title)