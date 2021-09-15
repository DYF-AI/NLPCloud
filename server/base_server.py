import sys
sys.path.append("..")

import fire
import uvicorn
import fastapi
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request

from base.word_segmentation.word_segmentation import word_segmentation_jieba

app = FastAPI(title='word_segmentation')

# 创建一个分词对象
word_seg = word_segmentation_jieba()

def word_segmentation_server(input:str):
    result = {}
    output = word_seg.cut(input)
    result["seg_result"] = output
    return result


@app.post('/word_segmentation')
async def word_segmentation_post(request: Request, data:dict=None):
    print("input：", data['input'])
    output = word_segmentation_server(data['input'])
    print("output:", output)
    return {"result": output}


# 服务
def run(host='192.168.1.102', service_port=10060):
    uvicorn.run(app='server.base_server:app', host=host, port=service_port, reload=True)  # reload=True

if __name__ == "__main__":
    
    fire.Fire()