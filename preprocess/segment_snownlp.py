from snownlp import SnowNLP
from tqdm import tqdm

def segment():
    input_dir = "../dataset/result/queries.result"
    output_dir = "../dataset/result/snownlp/normal_segmented_queries.result"
    with open("./keyword.txt", "r", encoding="utf8") as keyword_file:
        for line in keyword_file:
            # 使用SnowNLP的add_word方法添加自定义词语
            SnowNLP(line.strip()).words
    with open(input_dir, "r", encoding="utf8") as input_file, open(output_dir, "w", encoding="utf8") as output_file:
        for line in tqdm(input_file, desc="Processing", ncols=100):
            # 使用SnowNLP的分词功能
            s = SnowNLP(line)
            word_list = s.words
            output_file.write(" ".join(word_list)+"\n")
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    segment()
