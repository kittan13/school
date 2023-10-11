import matplotlib.pyplot as plt

# グラフの作成
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# データポイントに注釈を追加
plt.annotate('Important Point', xy=(2, 4), xytext=(3, 8),
             arrowprops=dict(facecolor='red', arrowstyle='->'))

# グラフの表示
plt.show()
