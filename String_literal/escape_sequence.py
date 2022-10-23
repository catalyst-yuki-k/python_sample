# エスケープシーケンスと意味
# https://docs.python.org/3/reference/lexical_analysis.html#literals
# 2.字句解析

# Escape Sequence | Meaning                        | Notes
# \<newline>      | Backslash and newline ignored  | (1)
# \\              | Backslash (\)                  |
# \'              | Single quote (')               |
# \"              | Double quote (")               |
# \a              | ASCII Bell (BEL)               |
# \b              | ASCII Backspace (BS)           |
# \f              | ASCII Formfeed (FF)            |
# \n              | ASCII Linefeed (LF)            |
# \r              | ASCII Carriage Return (CR)     |
# \t              | ASCII Horizontal Tab (TAB)     |
# \v              |ASCII Vertical Tab (VT)         |
# \ooo            | Character with octal value ooo | (2,4)
# \xhh            | Character with hex value hh    | (3,4)

# (1) A backslash can be added at the end of a line to ignore the newline:
# >>> 'This string will not include \
# ... backslashes or newline characters.'
# 'This string will not include backslashes or newline characters.'
# The same result can be achieved using triple-quoted strings, or parentheses and string literal concatenation.
# (2) As in Standard C, up to three octal digits are accepted.
# (3) Unlike in Standard C, exactly two hex digits are required.
# (4) In a bytes literal, hexadecimal and octal escapes denote the byte with the given value. In a string literal, these escapes denote a Unicode character with the given value.

# \	文字列を途中で改行する
print("To be, or not to be: \
that is the question.")

# \\ バックスラッシュ (\)
print("\\Hello World!\\")
# \Hello World!\

# \' 一重引用符 (')
print('today\'s special')

# \" 二重引用符 (")
print("\"Good morning, Frank,\" said Hal.")

# \a ベル文字(BEL)
# 本来の目的は、データの送信先にいるオペレータに何らかの通知（「今からメッセージを送る」など）するために、相手側のストックティッカーやテレタイプ端末のベル（電鈴）を鳴らすことである。
# 端末エミュレータでは、デスクトップ環境の警告と統合したり（例えばmacOSのターミナルはシステム警告音を出す）、音を出さずにウィンドウを点滅させたりする。
print("\a")

# \b ASCII バックスペース(BS)
print("Hello World!")
print("Hello World!\b")
# Hello World!

# \f ASCII 書式送り (FF)
print("\f")

# \n ASCII 行送り(LF)
print("Hello\nWorld!")
# Hello
# World!

# \r ASCII 復帰 (CR)
print("\r")

# \t ASCII 水平タブ(TAB)
print("Hello\tWorld!")
# Hello   World!

# \v ASCII 垂直タブ(VT)
print("Hello\vWorld!")
# Hello
# World!

# \ooo	8進数oooを持つASCII文字
print("\110\145\154\154\157\040\127\157\162\154\144\041")
# Hello World!

# \xhh	16進数hhを持つASCII文字
print("\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x21")
# Hello

# Escape sequences only recognized in string literals are:
# Escape Sequence | Meaning                                      | Notes
# \N{name}        | Character named name in the Unicode database | (5)
# \uxxxx          | Character with 16-bit hex value xxxx         | (6)
# \Uxxxxxxxx      | Character with 32-bit hex value xxxxxxxx     | (7)
#
# (5) Changed in version 3.3: Support for name aliases 1 has been added.
# (6) Exactly four hex digits are required.
# (7) Any Unicode character can be encoded this way. Exactly eight hex digits are required.

# \N{name}	Unicode データベース中で名前 name を持つ文字
print("\N{GREEK CAPITAL LETTER ETA}\
\N{GREEK SMALL LETTER EPSILON}\
\N{GREEK SMALL LETTER LAMDA}\
\N{GREEK SMALL LETTER LAMDA}\
\N{GREEK SMALL LETTER OMICRON}\
\N{GREEK CAPITAL LETTER OMEGA}\
\N{GREEK SMALL LETTER OMICRON}\
\N{GREEK SMALL LETTER RHO}\
\N{GREEK SMALL LETTER LAMDA}\
\N{GREEK SMALL LETTER DELTA}")

# \uxxxx	16ビットの16進数値xxxxを持つUnicode文字
print("\u0048\u0065\u006C\u006C\u006F\u0020\u0057\u006F\u0072\u006C\u0064\u0021")

# \Uxxxxxxxx	32ビットの16進数値xxxxxxxxを持つUnicode文字
print("\U00000048\U00000065\U0000006C\U0000006C\U0000006F\U00000020\U00000057\U0000006F\U00000072\U0000006C\U00000064\U00000021")