import jieba


# 分词工具： jieba

class word_segmentation(object):
    def __init__(self) -> None:
        super().__init__()
        pass

    def forward(self, input, cut_all=True):
        seg_list = jieba.cut(input, cut_all)
        return "" + "/ ".join(seg_list)


if __name__ == "__main__":
    input = "中国上海是一座美丽的国际性大都市"
    ws = word_segmentation()
    output = ws.forward(str(input))
    print(output)

