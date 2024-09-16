import matplotlib.pyplot as plt

# 示例数据
x_values = [1, 2, 3, 4]

y_values1 = [0.663, 0.675, 0.572, 0.286]
y_values2 = [0.666, 0.669, 0.572, 0.334]
y_values3 = [0.641, 0.793, 0.510, 0.282]
y_values4 = [0.629, 0.777, 0.562, 0.205]

# 画四根线的折线图
plt.plot(x_values, y_values1, marker='o', label='ori')
plt.plot(x_values, y_values2, marker='o', label='dist')
plt.plot(x_values, y_values3, marker='o', label='ordinal')
plt.plot(x_values, y_values4, marker='o', label='tol')

plt.xlabel('situationDE           situationPSD           subjectDE           subjectPSD')
plt.xticks([])

# 显示图例
plt.legend()

# 显示图形
plt.show()
