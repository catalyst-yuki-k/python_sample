# https://docs.python.org/ja/3/library/string.html
# string --- 一般的な文字列操作

# +演算子で文字列を結合できる
fruits = 'apple' + 'orange' + 'lemon'
print(fruits)
# appleorangelemon

# 変数に代入して結合も可能
fruit_1 = 'apple'
fruit_2 = 'orange'
fruit_3 = 'lemon'
fruits = fruit_1 + fruit_2 + fruit_3
print(fruits)
# appleorangelemon

# 変数とリテラルを混在することも可能
fruits = fruit_1 + fruit_2 + fruit_3 + 'strawberry'
print(fruits)
# appleorangelemonstrawberry

# 前方や途中に結合することも可能
fruits = 'strawberry' + fruit_1 + fruit_2 + fruit_3
print(fruits)
# strawberryappleorangelemon
fruits = fruit_1 + 'strawberry' + fruit_2 + fruit_3
print(fruits)
# applestrawberryorangelemon

# +=演算子(代入演算子)を使うことも可能
juice = fruit_1
juice += fruit_2
print(juice)
# appleorange

# *演算子で繰り返すことも可能
print(fruit_1 * 3)
# appleappleapple

# 単に文字列リテラルを並べるだけでも結合される
fruits = 'apple''orange''lemon'
print(fruits)
# appleorangelemon

# 間に空白やタブがあっても結合される
fruits = 'apple' 'orange'   'lemon'
print(fruits)
# appleorangelemon

# バックスラッシュで改行しても結合される
phrase = \
'Go to, let us go down, and there confound'\
'their language, that they may not understand'\
'one another’s speech.'
print(phrase)
# Go to, let us go down, and there confoundtheir language, that they may not understandone another’s speech.