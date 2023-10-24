import time

import segment_jieba
import segment_snownlp
from preprocess import segment_thulac, segment_pyltp


def main():
    # 记录jieba开始结束时间，输出总耗时与it/s
    start_time = time.time()
    print("开始jieba分词")
    segment_jieba.segmentKey()
    end_time = time.time()
    print("结束jieba分词")
    print("总耗时：", end_time - start_time, "s")
    print("it/s:", 21426941 / (end_time - start_time))
    print("--------------------------------------------")

    # 记录snowNLP开始结束时间，输出总耗时与it/s
    start_time = time.time()
    print("开始snowNLP分词")
    segment_snownlp.segmentKey()
    end_time = time.time()
    print("结束snowNLP分词")
    print("总耗时：", end_time - start_time, "s")
    print("it/s:", 21426941 / (end_time - start_time))
    print("--------------------------------------------")

    start_time = time.time()
    print("开始thulac分词")
    segment_thulac.segmentKey()
    end_time = time.time()
    print("结束thulac分词")
    print("总耗时：", end_time - start_time, "s")
    print("it/s:", 21426941 / (end_time - start_time))
    print("--------------------------------------------")

    start_time = time.time()
    print("开始pyltp分词")
    segment_pyltp.segmentKey()
    end_time = time.time()
    print("结束pyltp分词")
    print("总耗时：", end_time - start_time, "s")
    print("it/s:", 21426941 / (end_time - start_time))
    print("--------------------------------------------")



if __name__ == '__main__':
    main()