# -*- coding: gbk -*-
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 数据
tools = ['jieba', 'snowNLP', 'thulac', 'pyltp']
machine1_times = [123.71, 479.48, 175.64, 120.04]  # 第一台机器的分词时间
machine2_times = [127.47, 455.18, 191.00, 130.21]  # 第二台机器的分词时间
machine3_times = [39.05, 213.62,  65.86,  42.70]  # 第二台机器的分词时间
# 设置柱状图的宽度
bar_width = 0.2

# 设置X轴位置
x = range(len(tools))

# 创建子图
fig, ax = plt.subplots()

# 绘制第一台机器的数据
bar1 = ax.bar(x, machine1_times, bar_width, label='Machine 1')

# 绘制第二台机器的数据
bar2 = ax.bar([i + bar_width for i in x], machine2_times, bar_width, label='Machine 2')

# 绘制第三台机器的数据
bar3 = ax.bar([i + 2*bar_width for i in x], machine3_times, bar_width, label='Machine 3')

# 设置X轴标签
ax.set_xlabel('分词工具')
ax.set_ylabel('分词时间 (秒)')
ax.set_title('不同分词工具的分词时间比较')
ax.set_xticks(x)
ax.set_xticklabels(tools)


# 添加图例
ax.legend()

# 显示图表
plt.show()
