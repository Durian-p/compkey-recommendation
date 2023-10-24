import jieba
from tqdm import tqdm


def segmentKey():
    input_dir = "../dataset/result/queries.result"
    output_dir = "../dataset/result/jieba/normal_segmented_"
    keywords = []

    with open("./keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r", encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            jieba.add_word(keyword)
            keywords.append(keyword)

        for line in tqdm(input_file, desc="Processing", ncols=100):
            for keyword in keywords:
                if keyword in line.strip():
                    word_list = list(jieba.cut(line))  # 在此切换模式
                    with open(output_dir + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list))


if __name__ == '__main__':
    segmentKey()
