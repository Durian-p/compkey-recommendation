import os
from tqdm import tqdm
from pyltp import Segmentor
def segmentKey():
    input_dir = "../../dataset/result/2-extract/queries.result"
    output_dir = "../dataset/result/3-segment/pyltp/normal_segmented_"
    keywords = []
    output_dirs = []

    cws_model_path = os.path.join('../../ltp_data_v3.4.0', 'cws.model')  # 分词模型
    segmentor = Segmentor(cws_model_path, '../../keyword.txt')


    with open("../../keyword.txt", "r", encoding="utf8") as keyword_file, open(input_dir, "r", encoding="utf8") as input_file:
        for line in keyword_file:
            keyword = line.strip()
            keywords.append(keyword)
            output_dirs.append(output_dir + keyword + ".result")
        # 检查文件是否存在或不为空
        for output_file in output_dirs:
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                with open(output_file, 'w', encoding="utf8") as output_file:
                    # 清空文件内容
                    output_file.truncate()

        for line in tqdm(input_file, desc="Processing", ncols=100):
            for keyword in keywords:
                if keyword in line.strip():
                    word_list =  segmentor.segment(line.strip())  # 使用 pyltp 进行分词
                    with open(output_dir + keyword + ".result", "a", encoding="utf8") as output_file:
                        output_file.write(" ".join(word_list) + "\n")  # 写入换行符保持原始行结构

        segmentor.release()


if __name__ == '__main__':
    segmentKey()