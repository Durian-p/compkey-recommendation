def main():
    with open("keyword.txt", "r", encoding="utf8") as keyword_file:
        keywords = []
        for line in keyword_file:
            keyword = line.strip()
            keywords.append(keyword)
    for keyword in keywords:
        with open("dataset/result/3-segment/jieba/normal_segmented_" + keyword + ".result", "r",
                  encoding="utf8") as input_file:
            related_words = {}
            for line in input_file:
                words = line.split()
                for word in words:
                    if related_words.get(word) is None:
                        related_words[word] = 1
                    else:
                        related_words[word] += 1
        del related_words[keyword]

        total = 0
        for word in related_words:
            total += related_words[word]
        for word in related_words:
            related_words[word] = related_words[word] * 10000 / total
        related_words = dict(sorted(related_words.items(), key=lambda item: item[1], reverse=True))

        with open("dataset/result/4-intermediary/intermediary_key_" + keyword + ".result", "w",
                  encoding="utf8") as output_file:
            for word in related_words:
                output_file.write(word + " " + str(related_words[word]) + "\n")


if __name__ == '__main__':
    main()
