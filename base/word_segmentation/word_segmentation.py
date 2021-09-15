import jieba


# 分词工具： jieba

class word_segmentation_jieba(object):
    def __init__(self) -> None:
        super().__init__()
        print("创建分词对象")

    def cut(self, input:str, cut_all=True, dict_file=None):
        if dict_file:
            jieba.load_userdict(dict_file)
        seg_list = jieba.cut(input, cut_all)
        return "" + "/ ".join(seg_list)

    def cut_for_search(self, input:str, HMM=True):
        seg_list = jieba.cut_for_search(input, HMM)
        return "" + "/ ".join(seg_list)



if __name__ == "__main__":
    #input = "中国上海是一座美丽的国际性大都市"
    input = "奥利给，管虎执导的八佰是一部让人热血沸腾的好电影"
    ws = word_segmentation()
    output = ws.cut(str(input))
    print("cut: ", output)
    output = ws.cut_for_search(str(input))
    print("cut_for_search:", output)

    # add dict
    output = ws.cut(str(input), dict_file="dict.txt")
    print("dict cut: ", output)

