import matplotlib.pyplot as plt
import numpy as np

# 微分関数の定義
def de_da(a):
    return 20 * a - 10

# a軸の範囲を設定し、対応するde/da軸の値を計算
a_values = np.linspace(-4, 5, 500)
de_da_values = de_da(a_values)

# グラフを描画
plt.plot(a_values, de_da_values)
plt.xlabel('a')
plt.ylabel('de/da')
plt.title('de/da = 20a - 10')

# 罫線を表示
plt.grid()

# de/da = 0 の水平な直線を描画
plt.axhline(y=0, color='black', linestyle='-')

# a=1/2 の位置で水平線から真下に向かって線を引く
a_intersect = 1/2
plt.axvline(x=a_intersect, ymin=0, ymax=(de_da(a_intersect) - plt.ylim()[0]) / (plt.ylim()[1] - plt.ylim()[0]), color='r', linestyle='--')

# a=1/2 のメモリを追加
plt.annotate('a=1/2', xy=(a_intersect, plt.ylim()[0]), xytext=(a_intersect, plt.ylim()[0]), textcoords='data', ha='center', va='bottom', fontsize=10)

# ファイル出力
plt.savefig('de_da.pdf', format='pdf')
plt.savefig('de_da.png', format='png')

# グラフを表示
plt.show()
