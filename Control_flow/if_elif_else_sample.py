# 変数numberユーザーの入力を代入する
number = input('input number: ')
# ユーザーから受け取る入力は全て文字列となるため、整数に変換する
number = int(number)

# 変数numberが6の倍数の場合
if number % 6 == 0:
    print(number,'は6の倍数です。')
# 変数numberが3の倍数の場合
elif number % 3 == 0:
    print(number,'は3の倍数です。')
# 変数numberが2の倍数の場合
elif number % 2 == 0:
    print(number,'は2の倍数です。')
# 変数numberが2または3または6の倍数ではない場合
else:
    print(number,'は2または3または6の倍数ではありません。')