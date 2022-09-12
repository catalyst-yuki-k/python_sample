import requests
import bs4

# 変数urlを定義し、スクレイピングしたいWEBサイトのアドレスを渡す
target_url = 'https://info.finance.yahoo.co.jp/fx/convert/'

# requests.get()に対してurlを渡す
# requests.get()で指定されたwebの情報を取得し、結果を変数target_resに格納する
target_res = requests.get(target_url)

# Responseオブジェクトのステータスコードが200番台以外の場合は例外処理する
# （エラーメッセージを表示し、スクリプトを停止する）
target_res.raise_for_status()

# HTML文字列からBeautifulSoupオブジェクトを生成する
target_soup = bs4.BeautifulSoup(target_res.text, "html.parser")

# span要素を取り除く
for tag in target_soup.findAll(["span"]):
    # タグとその内容の削除
    tag.decompose()

# <td class="newest">の要素を取得する
newest_rate = target_soup.find("td", class_="newest").get_text()

# 取得した内容を表示する
print(str(newest_rate))
