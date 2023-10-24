# 竞争性关键词推荐算法实验仓库
## 1. 项目结构
- dataset/
  - origin/
    - SogouQ/  搜狗搜索日志数据集原始数据文件夹，GB18030编码
  - result/  数据处理结果
    - utf8/  原始数据集转utf8编码文件夹
    - **queries.result**  搜索字符串文件
    - **normal_segmented_queries.result**  搜索字符串分词文件(精确模式)
    - **search_segmented_queries.result**  搜索字符串分词文件(搜索模式)


- preprocess/  数据预处理代码文件夹
  - **convert_encoding.py**  编码转换
  - **extract_queries.py**  提取搜索字符串
  - **segment.py**  分词

## 2. 项目依赖
python3.9

jieba==0.42.1

tqdm==4.66.1