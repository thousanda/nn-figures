import matplotlib.pyplot as plt
import numpy as np

# 関数の定義
def e(a):
    return 10 * a**2 - 10 * a + 2.525

# a軸の範囲を設定し、対応するe軸の値を計算
a_values = np.linspace(-4, 5, 500)
e_values = e(a_values)

# グラフを描画
plt.plot(a_values, e_values)
plt.xlabel('a')
plt.ylabel('e')
plt.title('e = 10a^2 - 10a + 2.525')
plt.grid()

# ファイル出力
plt.savefig('error.pdf', format='pdf')
plt.savefig('error.png', format='png')

# グラフを表示
plt.show()
