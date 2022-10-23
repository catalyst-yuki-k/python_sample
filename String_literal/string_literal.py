# https://peps.python.org/pep-0008/
# https://peps.python.org/pep-0008/#string-quotes
#
# PEP 8 – Style Guide for Python Code
# PEP 8 – Python コードのスタイルガイド
#
# In Python, single-quoted strings and double-quoted strings are the same. 
# This PEP does not make a recommendation for this. 
# Pick a rule and stick to it. 
# When a string contains single or double quote characters, 
# however, use the other one to avoid backslashes in the string. 
# It improves readability.
# Python では、単一引用符で囲まれた文字列と二重引用符で囲まれた文字列は同じです。
# この PEP は、これを推奨するものではありません。
# ルールを選び、それを守りましょう。
# ただし、文字列に一重引用符または二重引用符が含まれている場合は、
# もう一方を使用して文字列内のバックスラッシュを回避してください。
# 可読性が向上します。

# 文字列をprintする場合はダブルクオーテーション("")で囲む
print("Hello world!")
# シングルクオーテーション('')で囲んでも良い
print('Hello world!')

# 文字列中でシングルクオーテーションを使いたい場合は、全体をダブルクオーテーション("")で囲む
# シングルクオーテーションをシングルクオーテーションで囲むとエラーが出る
# これはシングルクオーテーションを入れ子ではなく並列として処理されるからである
#  File "c:\github\repository\python_sample\String_literal\string_literal.py", line 6
#    print('today's special')
#                          ^
#SyntaxError: invalid syntax
print("today's special")
# シングルクオーテーション('')で囲む場合は文字列中の'をバックスラッシュ(環境によっては半角の￥)でエスケープする
print('today\'s special')

# 文字列中でダブルクオーテーションを使いたい場合は、全体をシングルクオーテーション('')で囲む
# ダブルクオーテーションをダブルクオーテーションで囲むとエラーが出る
# これはダブルクオーテーションを入れ子ではなく並列として処理されるからである
#  File "c:\github\repository\python_sample\String_literal\string_literal.py", line 26
#    print(""Good morning, Frank," said Hal.")
#          ^^^^^^
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('"Good morning, Frank," said Hal.')
# ダブルクオーテーション("")で囲む場合は文字列中の"をバックスラッシュ(環境によっては半角の￥)でエスケープする
print("\"Good morning, Frank,\" said Hal.")

# 長い文字列を途中で改行して入力する場合には、改行の前に \ を記述する
print("To be, or not to be: \
that is the question.")