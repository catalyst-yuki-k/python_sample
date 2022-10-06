# 変数numberユーザーの入力を代入する
number = input('input number: ')
# ユーザーから受け取る入力は全て文字列となるため、整数に変換する
number = int(number)

# 変数numberが偶数の場合
if number % 2 == 0:
    # 画面に表示する
    print('偶数です')