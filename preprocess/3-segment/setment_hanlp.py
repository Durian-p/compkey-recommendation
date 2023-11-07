from pyhanlp import HanLP
from tqdm import tqdm
import os

def segmentKey():
    input_dir = "../../dataset/result/2-extract/queries.result"
    output_dir_prefix = "../dataset/result/3-segment/hanlp/normal_segmented_"
    keywords = []
    output_dirs = []
    with open("../../keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r", encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            HanLP.Config.CustomDictionary.add(keyword)  # 添加用户自定义词汇
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
                    word_list = HanLP.segment(line.strip())  # 使用HanLP进行分词
                    word_list = [term.word for term in word_list]  # 获取分词结果中的词语部分
                    with open(output_dir_prefix + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list) + "\n")  # 写入换行符保持原始行结构


if __name__ == '__main__':
    segmentKey()
