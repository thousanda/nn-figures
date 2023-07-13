import matplotlib.pyplot as plt

data = ((1, 0.7), (2, 1.0), (3, 1.2), (4, 2.2), (5, 2.3), (6, 3.0), (7, 3.2), (8, 4.4), (9, 4.4), (10, 5.1))

# 散布図を描画
x, y = zip(*data)
plt.scatter(x, y, label='Data points')

# y軸の範囲を指定
plt.ylim(-1, 24)

# 直線 y = 2x を描画
x_line = range(0, 12)
y_line = [2*i for i in x_line]
plt.plot(x_line, y_line, color='red', label='y=ax')

# グラフの設定
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# グリッドをデータポイントの下に表示する
ax = plt.gca()
ax.set_axisbelow(True)
ax.grid()

plt.title('Regression with y=2x')

# ファイル出力
plt.savefig('regression_2x.pdf', format='pdf')
plt.savefig('regression_2x.png', format='png')

# グラフを表示
plt.show()
