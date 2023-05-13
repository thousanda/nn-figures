import matplotlib.pyplot as plt
import numpy as np

# 勾配っぽい適当な関数の定義
def gradient(x):
    return  0.1*x**5 + 0.7*x**4 - 3*x**3 - 8*x**2 + 6*x - 5

# x軸の範囲を設定し、対応するy軸の値を計算
x_values = np.linspace(-4, 4, 500)
y_values = gradient(x_values)

# グラフを描画
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('de/dw')
plt.title('Gradient')
plt.grid()

# ファイル出力
plt.savefig('gradient.pdf', format='pdf')
plt.savefig('gradient.png', format='png')

# グラフを表示
plt.show()
