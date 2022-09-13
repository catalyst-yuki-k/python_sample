import urllib.request, urllib.error
import lxml.html
import bs4

url = 'https://info.finance.yahoo.co.jp/fx/convert/'
# 指定したurlのサイトを開く
html = urllib.request.urlopen(url=url)
print('url:', html.geturl())
print('code:', html.getcode())
print('Content-Type:', html.info()['Content-Type'])
# read()で読み込む
html = html.read()
#そのままだとマルチバイト文字がエスケープされているので、decode()する
html = html.decode()

# 取得した内容を表示する
print(str(html))