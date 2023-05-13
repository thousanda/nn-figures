import matplotlib.pyplot as plt

data = ((1, 0.7), (2, 1.0), (3, 1.2), (4, 2.2), (5, 2.3), (6, 3.0), (7, 3.2), (8, 4.4), (9, 4.4), (10, 5.1))

# 散布図を描画
x, y = zip(*data)
plt.scatter(x, y, label='Data points')

# 直線 y = 3x を描画
x_line = range(0, 12)
y_line = [(1/2) * i for i in x_line]
plt.plot(x_line, y_line, color='red', label='y=ax')

# 各データポイントから y = 3x に対して y軸に平行な直線を引く
for point_x, point_y in data:
    y_intersection = (1/2) * point_x
    plt.plot([point_x, point_x], [point_y, y_intersection], linestyle='--', color='dimgray')

# グラフの設定
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# グリッドをデータポイントの下に表示する
ax = plt.gca()
ax.set_axisbelow(True)
ax.grid()

plt.title('Regression with y=ax')

# ファイル出力
plt.savefig('distance.pdf', format='pdf')
plt.savefig('distance.png', format='png')

# グラフを表示
plt.show()
