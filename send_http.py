
import requests
url="http://tsn.baidu.com/text2audio"
data={
    'tex':'你好',
    'lan':'zh',
    'ctp':'1',
    'vol':'15',
    'per':'0',
    'cuid':'20b4f1f1179a2471c86deff14ddc9569',
    'tok':'24.d4e4601ce1029abe1ed36f28da09f17d.2592000.1603090749.282335-22120812'
}

res=requests.post(url=url,data=data)
print(res.content)
with open("1.mp3",'wb') as f:
    f.write(res.content)