import matplotlib.pyplot as plt
import numpy as np

# sigmoid関数の定義
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# x軸の範囲を設定し、対応するy軸の値を計算
x_values = np.linspace(-10, 10, 500)
y_values = sigmoid(x_values)

# グラフを描画
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.title('Sigmoid Function')
plt.grid()

# ファイル出力
plt.savefig('sigmoid.pdf', format='pdf')
plt.savefig('sigmoid.png', format='png')

# グラフを表示
plt.show()
