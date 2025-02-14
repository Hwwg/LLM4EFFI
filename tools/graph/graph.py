import numpy as np
import matplotlib.pyplot as plt

# 数据
groups = ["Easy", "Medium", "Hard"]
value1 = [83.11, 81.39, 75.26]
value2 = [81.26, 81.88, 73.55]
value3 = [69.39, 74.31, 46.76]
value4 = [87.49, 83.71, 77.08]

# 计算增量
def calculate_difference(base, values):
    return [round(v - base[i], 2) for i, v in enumerate(values)]

diff2 = calculate_difference(value1, value2)
diff3 = calculate_difference(value1, value3)
diff4 = calculate_difference(value1, value4)

# 绘图设置
bar_width = 0.23  # 增加柱子宽度
index = np.arange(len(groups))

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制柱状图
plt.bar(index, value1, bar_width, label='Original', edgecolor='black', color="#FADCAA", hatch="//")
plt.bar(index + bar_width, value2, bar_width, label='Effilearner', edgecolor='black', color="#A6D0DD", hatch="..")
plt.bar(index + 2 * bar_width, value3, bar_width, label='ECCO', edgecolor='black', color="#82A0D8", hatch="--")
plt.bar(index + 3 * bar_width, value4, bar_width, label='LLM4EFFI', edgecolor='black', color="#CABBE9", hatch="\\")

# 设置Y轴范围
plt.ylim(0, 100)

# 添加轴标签和图例
# plt.xlabel('Groups', fontsize=15)
plt.ylabel('Beyond@1', fontsize=15)
plt.xticks(index + 1.5 * bar_width, groups, fontsize=15)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=15)

# 在每个柱子上标注数值和增量
def add_labels(x, values, diffs, is_bold=False):
    for i, (v, d) in enumerate(zip(values, diffs)):
        plt.text(x[i], v + 1, f"{v}", ha='center', va='bottom', fontsize=10, color='black')  # 标注数值
        if d >= 0:
            plt.text(x[i], v + 5, f"(+{d})", ha='center', va='bottom', fontsize=10, color='green', fontweight='bold' if is_bold else 'normal')  # 绿色标注增量
        else:
            plt.text(x[i], v + 5, f"({d})", ha='center', va='bottom', fontsize=10, color='red', fontweight='bold' if is_bold else 'normal')  # 红色标注减少量

# 标注 value1 的数值
for i, v in enumerate(value1):
    plt.text(index[i], v + 1, f"{v}", ha='center', va='bottom', fontsize=10, color='black')

# 标注 value2、value3、value4 的数值和增量
add_labels(index + bar_width, value2, diff2)
add_labels(index + 2 * bar_width, value3, diff3)
add_labels(index + 3 * bar_width, value4, diff4, is_bold=True)  # LLM4EFFI 的增量加粗

# 保存为 PDF
plt.savefig('Mercury.pdf', format='pdf', bbox_inches='tight')

# 显示图表
plt.show()