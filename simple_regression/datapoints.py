import matplotlib.pyplot as plt

data = ((1, 0.7), (2, 1.0), (3, 1.2), (4, 2.2), (5, 2.3), (6, 3.0), (7, 3.2), (8, 4.4), (9, 4.4), (10, 5.1))

# 散布図を描画
x, y = zip(*data)
plt.scatter(x, y, label='Data points')

# 描画範囲を指定
plt.xlim(-0.6, 11.6)  # x軸の範囲を指定
plt.ylim(-0.3, 5.8)  # y軸の範囲を指定

# グラフの設定
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# グリッドをデータポイントの下に表示する
ax = plt.gca()
ax.set_axisbelow(True)
ax.grid()

plt.title('Data points')

# ファイル出力
plt.savefig('datapoints.pdf', format='pdf')
plt.savefig('datapoints.png', format='png')

# グラフを表示
plt.show()
