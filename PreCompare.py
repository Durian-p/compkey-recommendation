from tqdm import tqdm
def pre():
    file_path = "dataset/result/jieba/jieba.result"
    keywords = []
    with open("keyword.txt", "r", encoding="utf8") as keyword_file:
        for line in keyword_file:
            keyword = line.strip()
            keywords.append(keyword)

    for keyword in keywords:
        fans = {}
        with open("dataset/result/4-intermediary/intermediary_key_" + keyword + ".result", "r", encoding="utf8") as file:

            lines = file.readlines()
            for line in tqdm(lines, desc="Processing", ncols=100):

                parts = line.strip().split()
                if float(parts[1]) / 10000.0 < 0.0001 :
                    continue
                dic = {}
                with open(file_path,"r",encoding="utf8") as datafile:
                    lines2 = datafile.readlines()
                    for line2 in lines2:

                            dictmp = {}
                            words = line2.strip().split()
                            if parts[0] in words:
                                for word in words:
                                    dictmp[word] = 1
                                keys = dictmp.keys()
                                for key in keys:
                                    if dic.get(key) is None:
                                        dic[key] = 1
                                    else:
                                        dic[key] += 1
                for key,val in dic.items():
                    if dic.get(keyword) is None:
                        continue
                    if key != keyword and key != parts[0] :
                        if fans.get(key) is None:
                            fans[key] = val / (dic[parts[0]] - dic[keyword])
                        else:
                            fans[key] += val / (dic[parts[0]] - dic[keyword])

        with open("dataset/result/5-final/intermediary_key_" + keyword + ".result", "w",
                  encoding="utf8") as output_file:

            dict(sorted(fans.items(), key=lambda item: item[1], reverse=True))
            for key,val in fans.items():
                print(key + " " + str(val) + "\n")
                output_file.write(key + " " + str(val) + "\n")

if __name__ == '__main__':
    pre()





