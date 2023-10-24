# -*- coding: gbk -*-
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# ����
tools = ['jieba', 'snowNLP', 'thulac', 'pyltp']
machine1_times = [123.71, 479.48, 175.64, 120.04]  # ��һ̨�����ķִ�ʱ��
machine2_times = [127.47, 455.18, 191.00, 130.21]  # �ڶ�̨�����ķִ�ʱ��
machine3_times = [39.05, 213.62,  65.86,  42.70]  # �ڶ�̨�����ķִ�ʱ��
# ������״ͼ�Ŀ��
bar_width = 0.2

# ����X��λ��
x = range(len(tools))

# ������ͼ
fig, ax = plt.subplots()

# ���Ƶ�һ̨����������
bar1 = ax.bar(x, machine1_times, bar_width, label='Machine 1')

# ���Ƶڶ�̨����������
bar2 = ax.bar([i + bar_width for i in x], machine2_times, bar_width, label='Machine 2')

# ���Ƶ���̨����������
bar3 = ax.bar([i + 2*bar_width for i in x], machine3_times, bar_width, label='Machine 3')

# ����X���ǩ
ax.set_xlabel('�ִʹ���')
ax.set_ylabel('�ִ�ʱ�� (��)')
ax.set_title('��ͬ�ִʹ��ߵķִ�ʱ��Ƚ�')
ax.set_xticks(x)
ax.set_xticklabels(tools)


# ���ͼ��
ax.legend()

# ��ʾͼ��
plt.show()
