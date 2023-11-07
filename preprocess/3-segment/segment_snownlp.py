from snownlp import SnowNLP
from tqdm import tqdm
import os


def segmentKey():
    input_dir = "../../dataset/result/2-extract/queries.result"
    output_dir_prefix = "../dataset/result/3-segment/snownlp/normal_segmented_"
    keywords = []
    output_dirs = []
    with open("../../keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r",
                                                                               encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            keywords.append(keyword)
            output_dirs.append(output_dir_prefix + keyword + ".result")

        # 检查文件是否存在或不为空
        for output_file in output_dirs:
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                with open(output_file, 'w', encoding="utf8") as output_file:
                    # 清空文件内容
                    output_file.truncate()

        for line in tqdm(input_file, desc="Processing", ncols=100):
            for keyword in keywords:
                if keyword in line.strip():
                    s = SnowNLP(line)  # 使用SnowNLP分词
                    word_list = s.words
                    with open(output_dir_prefix + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list) + "\n")


if __name__ == '__main__':
    segmentKey()
