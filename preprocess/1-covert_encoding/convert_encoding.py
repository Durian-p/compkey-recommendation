import codecs
from tqdm import tqdm


def convert_encoding():
    # 统一的目标编码
    target_encoding = "utf-8"

    for i in tqdm(range(1, 32), ncols=100):
        if i == 25:
            continue
        if i < 10:
            input_file = "../../dataset/origin/SogouQ/access_log.2006080" + str(i) + ".decode.filter"
            output_file = "../../dataset/result/1-convert/access_log.2006080" + str(i) + ".decode.filter"
        else:
            input_file = "../../dataset/origin/SogouQ/access_log.200608" + str(i) + ".decode.filter"
            output_file = "../../dataset/result/1-convert/access_log.200608" + str(i) + ".decode.filter"
        print(input_file)
        print(output_file)

        with open(input_file, "rb") as input_file, codecs.open(output_file, "w", target_encoding) as output_file:
            try:
                content = input_file.read()
                # 将文件内容转换为UTF-8编码并写入输出文件
                output_file.write(content.decode("gb18030", errors="ignore"))
                print(f"Converted {input_file} to {target_encoding}")
            except Exception as e:
                print(f"Error processing {input_file}: {str(e)}")

    print("Conversion complete.")


if __name__ == '__main__':
    convert_encoding()
