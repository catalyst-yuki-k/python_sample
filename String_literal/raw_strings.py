# https://docs.python.org/ja/3/reference/lexical_analysis.html

# 「\」を表示したい場合はエスケープシーケンスを使う
print("Pythonがインストールされた場所は C:\\Python310\\python.exe です")

# 「r」をつけることで、「\」はエスケープシーケンスを使わなくても表示できる。
print(r"Pythonがインストールされた場所は C:\Python310\python.exe です")

# 「R」をつけることでも同じ効果が得られる。
print(R"Pythonがインストールされた場所は C:\Python310\python.exe です")

# 文字列リテラルとバイト列リテラルの両方は、任意で文字 'r' または 'R' をプレフィックスに持つことができます
# そのような文字列は raw strings と呼ばれ、バックスラッシュをリテラル文字として扱います。
# その結果、文字列リテラルでは raw 文字列中の '\U' と '\u' のエスケープは特別扱いされません。 
# Python 2.x の raw unicode リテラルが Python 3.x とは異なる振る舞いをするため、 'ur' 構文はサポートされません。

# raw リテラルでも、引用符はバックスラッシュでエスケープできますが、バックスラッシュ自体も文字列に残ります
# 例えば、r"\"" は有効な文字列リテラルで、バックスラッシュと二重引用符からなる文字列を表します
# r"\" は無効な文字列リテラルです (raw リテラルを奇数個連なったバックスラッシュで終わらせることはできません)。
# 具体的には、(バックスラッシュが直後のクオート文字をエスケープしてしまうので) raw文字列を単一のバックスラッシュで終わらせることはできません
# さらに、バックスラッシュの直後に改行がきても、行継続を意味する のではなく、リテラルの一部であるそれら二つの文字として解釈されます。