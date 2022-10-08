seasons = ['apple', 'orange', 'banana', 'pineapple']
target = 'apple'
found = False

print('リストから',target,'を含む単語を探索します')

for season in seasons:
    if target in season:
        found = True
        print(f'リストに発見しました: {season}')
        continue

if not found:
    print('リストにはありませんでした')