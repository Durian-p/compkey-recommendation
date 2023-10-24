import jieba
from tqdm import tqdm


def segment():
    input_dir = "../dataset/result/queries.result"
    output_dir = "../dataset/result/normal_segmented_queries.result"
    with open("./keyword.txt", "r", encoding="utf8") as keyword_file:
        for line in keyword_file:
            jieba.add_word(line.strip())
    with open(input_dir, "r", encoding="utf8") as input_file, open(output_dir, "w", encoding="utf8") as output_file:
        for line in tqdm(input_file, desc="Processing", ncols=100):
            word_list = list(jieba.cut(line))  # 在此切换模式
            output_file.write(" ".join(word_list))
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    segment()