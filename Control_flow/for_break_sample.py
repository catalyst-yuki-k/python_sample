seasons = ['春', '夏', '秋', '冬']
target = '秋'

print('リストから',target,'を探索します')

for season in seasons:
    if target in season:
        print(f'リストに発見しました: {season}')
        break
else:
    print('リストにはありませんでした')