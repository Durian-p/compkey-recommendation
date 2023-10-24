import thulac
from tqdm import tqdm
def segmentKey():
    input_dir = "../dataset/result/queries.result"
    output_dir = "../dataset/result/thulac/normal_segmented_"
    keywords = []

    thu = thulac.thulac(user_dict='./keyword.txt',seg_only=True)  # 初始化THULAC

    with open("./keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r", encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            keywords.append(keyword)

        for line in tqdm(input_file, desc="Processing", ncols=100):
            for keyword in keywords:
                if keyword in line.strip():
                    word_list = thu.cut(line.strip(), text=True).split()  # 使用THULAC进行分词
                    with open(output_dir + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list) + "\n")  # 写入换行符保持原始行结构
if __name__ == '__main__':
    segmentKey()