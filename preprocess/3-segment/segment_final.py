import jieba
from tqdm import tqdm
import jieba.posseg as pseg
import os
import re


# 定义一个函数，加载指定目录下的所有txt文件作为词库
def load_custom_dicts_from_directory(directory):
    custom_dict_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

    for dict_file in custom_dict_files:
        dict_path = os.path.join(directory, dict_file)
        jieba.load_userdict(dict_path)
        print(f"Loaded custom dictionary from {dict_path}")


def clean_special_characters(text):
    # 去除书名号
    text = re.sub(r'《|》', '', text)
    # 去除标点符号和特殊字符
    text = re.sub(r'[^\w\s]', '', text)
    return text


def segmentKey():
    # 词库处理完毕，jieba读取词典
    custom_dict_directory = "D:\\program\\machine\\compkey\\dataset\\result\\worddict"
    # 加载自定义词典文件
    load_custom_dicts_from_directory(custom_dict_directory)
    # 启用缓存以加速分词
    # jieba.enable_paddle()  # 启用paddle模式

    input_dir = "../../dataset/result/2-extract/queries.result"
    output_dir = "../../dataset/result/3-segment/segmented_all.result"
    keywords = []
    output_dirs = []

    # 检查文件是否存在或不为空
    for output_file in output_dirs:
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            with open(output_file, 'w', encoding="utf8") as output_file:
                # 清空文件内容
                output_file.truncate()

    with open(input_dir, "r", encoding="utf8") as input_file, open(output_dir, "w", encoding="utf8") as output_file:
        for line in tqdm(input_file, desc="Processing", ncols=100):
            line = clean_special_characters(line)
            word_list = []
            words_with_pos = pseg.cut(line)  # 在此切换模式
            for word, pos in words_with_pos:
                # 根据词性过滤掉不需要的词语
                if pos in ["u"]:  # 助词 语气词
                    continue
                word_list.append(word)
                output_file.write(" ".join(word_list))

if __name__ == '__main__':
    segmentKey()
