from selenium import webdriver

# 変数urlを定義し、スクレイピングしたいWEBサイトのアドレスを渡す
target_url = 'https://info.finance.yahoo.co.jp/fx/convert/'
# chromedriver.exeの置き場所
webdriver_path="C:/chromedriver_win32_v105/chromedriver.exe"
# xpathの定義
full_xpath = '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[3]'
# chromedriver.exeの読み込み
driver = webdriver.Chrome(webdriver_path)
# Webサイトにアクセスする
driver.get(target_url)
# ページのソースを取得する
driver.page_source
# ページの「最新取引レート」の要素を取得する
newest_rate = driver.find_element_by_xpath(full_xpath) # xpathでの指定
# find_element_by_xpathからtext要素のみ取り出す
newest_rate = newest_rate.text

# 取得した内容を改行コードで分割した配列に代入する
newest_rate_matrix = newest_rate.splitlines()
# 配列の0番目の要素を表示する
print(str(newest_rate_matrix[0]))

# ヘッドレスブラウザを閉じる
driver.close()
