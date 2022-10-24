# https://peps.python.org/pep-0257/
# PEP 257 – Docstring 規約

# 文章を改行するためには改行を表すエスケープシーケンス「\n」が必要
print("Go to, let us go down, and there confound\ntheir language, that they may not understand\none another’s speech.")

# 三連引用符で囲むと、三連引用符内の改行がそのままターミナルに反映される
print("""Go to, let us go down, and there confound
their language, that they may not understand
one another’s speech.""")

# 行の頭をそろえるために三連引用符直後で改行すると、ターミナルの１行目には不要な空白行が表示されてしまう
print("""
Go to, let us go down, and there confound
their language, that they may not understand
one another’s speech.""")

# そこで「\」と組合せて下記のように記述すると、不要な空白行が表示されずに済む
print("""\
Go to, let us go down, and there confound
their language, that they may not understand
one another’s speech.""")

# 代入することも可能
phrase = """\
Go to, let us go down, and there confound
their language, that they may not understand
one another’s speech."""

print(phrase)

