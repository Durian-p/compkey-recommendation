# 读取目标文本文件

output_file = "../dataset/queries.result"

# 打开输出文件
with open(output_file, "w", encoding="utf-8") as output_file:
    for i in range(1, 32):
        if i == 25:
            continue
        if i < 10:
            input_file = "../dataset/result/utf8/access_log.2006080" + str(i) + ".decode.filter"
        else:
            input_file = "../dataset/result/utf8/access_log.200608" + str(i) + ".decode.filter"
        print(input_file)
        # 打开目标文本文件
        with open(input_file, "r", encoding="utf8") as input_file:
            # 逐行读取目标文本文件
            for line in input_file:
                # 分割每一行记录
                parts = line.split('\t')
                if len(parts) >= 3:
                    # 提取查询词并去除首尾空格
                    query = parts[1].strip().replace('[','').replace(']','')
                    # 追加查询词到输出文件
                    output_file.write(query + "\n")

# 关闭输出文件
output_file.close()
