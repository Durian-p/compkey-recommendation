import jieba
from tqdm import tqdm
import os
import re

# 定义一个函数，加载指定目录下的所有txt文件作为词库
def load_custom_dicts_from_directory(directory):
    custom_dict_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

    for dict_file in custom_dict_files:
        dict_path = os.path.join(directory, dict_file)
        jieba.load_userdict(dict_path)
        print(f"Loaded custom dictionary from {dict_path}")


def segmentKey():
    # 词库处理完毕，jieba读取词典
    custom_dict_directory = "D:\\program\\machine\\compkey\\dataset\\result\\worddict"
    # 加载自定义词典文件
    load_custom_dicts_from_directory(custom_dict_directory)
    # 启用缓存以加速分词
    jieba.enable_paddle()  # 启用paddle模式


    input_dir = "../../dataset/result/2-extract/queries.result"
    output_dir_prefix = "../../dataset/result/3-segment/jieba/normal_segmented_"
    keywords = []
    output_dirs = []
    with open("../../keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r",
                                                                               encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            jieba.add_word(keyword)
            keywords.append(keyword)
            output_dirs.append(output_dir_prefix + keyword + ".result")
        # 检查文件是否存在或不为空
        for output_file in output_dirs:
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                with open(output_file, 'w', encoding="utf8") as output_file:
                    # 清空文件内容
                    output_file.truncate()

        # 寻找关键字并分词
        for line in tqdm(input_file, desc="Processing", ncols=100):
            for keyword in keywords:
                if keyword in line.strip():
                    word_list = list(jieba.cut(line))  # 在此切换模式
                    with open(output_dir_prefix + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list))

if __name__ == '__main__':
    segmentKey()
