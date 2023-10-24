import os

import jieba
import pyltp
import thulac
from tqdm import tqdm
from pyltp import Segmentor
from pyltp  import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

def segmentKeyJieBa():
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




def segmentKeyTHULAC():
    input_dir = "../dataset/result/queries.result"
    output_dir = "../dataset/result/thulac/normal_segmented_"
    keywords = []

    thu = thulac.thulac(seg_only=True)  # 初始化THULAC

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
def segmentKeyPyltp():
    input_dir = "../dataset/result/queries.result"
    output_dir = "../dataset/result/pyltp/normal_segmented_"
    keywords = []

    cws_model_path = os.path.join('../ltp_data_v3.4.0', 'cws.model')  # 分词模型
    segmentor = Segmentor(cws_model_path)


    with open("./keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r", encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            keywords.append(keyword)

        for line in tqdm(input_file, desc="Processing", ncols=100):
            for keyword in keywords:
                if keyword in line.strip():
                    word_list =  segmentor.segment(line.strip())  # 使用 pyltp 进行分词
                    with open(output_dir + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list) + "\n")  # 写入换行符保持原始行结构


if __name__ == '__main__':
    segmentKeyPyltp()
