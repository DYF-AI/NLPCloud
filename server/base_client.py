
import os
import fire
import requests

def post_data(host:str, port:str, api:str, data:dict):
    url = f"http://{host}:{port}/{api}"
    res = requests.post(url=url,json=data)
    return res.json()

def demo():
    host = "192.168.1.102"
    port = "10060"
    api = "word_segmentation"
    input = "奥利给，管虎执导的八佰是一部让人热血沸腾的好电影"
    data = {"input":input}
    res = post_data(host, port, api, data)
    print(res)

if __name__ == "__main__":
    import fire
    fire.Fire()