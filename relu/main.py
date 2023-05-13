import matplotlib.pyplot as plt
import numpy as np

# ReLU関数の定義
def relu(x):
    return np.maximum(0, x)

# x軸の範囲を設定し、対応するy軸の値を計算
x_values = np.linspace(-10, 10, 500)
y_values = relu(x_values)

# グラフを描画
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.title('ReLU Function')
plt.grid()

# ファイル出力
plt.savefig('relu.pdf', format='pdf')
plt.savefig('relu.png', format='png')

# グラフを表示
plt.show()
