# # import requests
#
# # url = "https://www.baidu.com"
# # response = requests.get(url)
#
# # # 1.打印服务器返回的响应状态码
# # print(response.status_code)
# # # 2.打印服务器返回的响应内容 , 全部
# # print(response.text)
# # # 5.设置编码格式
# # response.encoding = 'utf-8'
# # # 3.保存到一个html文件
# # with open("./baidu.html",mode="w",encoding="utf-8") as f:
# #     f.write(response.text)
# # import requests
# # url = "https://i0.hdslb.com/bfs/album/ebe4a66b4e0b60b1184ffaf7919b31edf12261ca.png"
# # response = requests.get(url)
# # print(response.content,type(response.content))
# # with open("1.png",mode="wb") as f:
# #     f.write(response.content)
#
# import requests
#
# burp0_url = "http://47.99.241.235:8092/login"
# burp0_headers = {"Accept": "*/*", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://47.99.241.235:8092", "Referer": "http://47.99.241.235:8092/toLogin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "close"}
# burp0_data = {"userName": "admin", "password": "123456"}
# response = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
# d = response.json()
# print(d,type(d))
# print(d['code'])
# print(d['msg'])
