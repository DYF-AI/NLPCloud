
import os
import requests

host = "192.168.1.102"

port = "10060"

url = f"http://{host}:{port}/word_segmentation"

input = "奥利给，管虎执导的八佰是一部让人热血沸腾的好电影"
data = {"input":input}
res = requests.post(url=url,json=data)
print(res.text)