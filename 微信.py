#Author:xubojoy
#展示比例一般使用百分比圆饼表吧

# 使用echarts，加上这段
from echarts import Echart, Legend, Pie
import itchat

# 先登录
itchat.login()

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 总数算上，好计算比例啊～
total = len(friends[1:])

chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()



import re

tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)

# 拼接字符串
text = "".join(tList)

# jieba分词
import jieba
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image

# 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         max_font_size=40, random_state=42,
                         font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf').generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


#以图片生成配色方案
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# import os
# import numpy as np
# import PIL.Image as Image
#
#
# d = os.path.dirname(__file__)
# alice_coloring = np.array(Image.open(os.path.join(d, "lv.jpg")))
# my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
#                          max_font_size=40, random_state=42,
#                          font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf')\
#     .generate(wl_space_split)
#
# image_colors = ImageColorGenerator(alice_coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
#
# # 保存图片 并发送到手机
# my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))
# itchat.send_image("wechat_cloud.png", 'filehelper')