


# 图片保存第三种方法
#
# from PIL import Image  #要按照pillow
# from io import BytesIO
# import requests
# url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531916396&di=0fb829b44c1988dd3a9afaea6881c28f&imgtype=jpg&er=1&src=http%3A%2F%2Fwww.th7.cn%2Fd%2Ffile%2Fp%2F2016%2F03%2F04%2F900fcb61946ee16040edaddd9303e8ae.jpg"
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# img.save('/home/karson/pps/img.jpg') # 图片下载路径和格式！

# img.save("/home/karson/pps/r.pdf")  # 图片也可以保存成pdf格式！

# 等于说用读取原始响应后，自己决存储的路径，顺便把格式决定了！




# 图片下载的第二种方法  也行不通，只能用文件读取的方式
# urllib.request.urlretrieve(url,"/home/karson/pps/img.jpg")



# 图片下载，图片链接遭遇反爬虫！
import requests
import urllib.request
proxies = { "https": "https://101.236.60.48"}

url = "http://ww3.sinaimg.cn/mw600/0073ob6Pgy1ft4ymak4qgj30jd0vjq94.jpg"
response = requests.get(url,stream= True,proxies=proxies)
with open("/home/karson/pps/%s.jpg" % url[-10:-1] ,"wb") as f :
    f.write(response.content)
    f.close()




# 以二进制数据写入图片，简单图像处理（图片->二进制->图片）


# 保存pdf文件
#
# url = "https://cran.usthb.dz/web/packages/argon2/argon2.pdf"
#
#
# import requests
# import os
# import re
# import urllib.requests
#
#
# def getFile(url):
#     file_name = url.split('/')[-1]
#     u = urllib.request.urlopen(url)
#     f = open(file_name, 'wb')
#
#     block_sz = 8192
#     while True:
#         buffer = u.read(block_sz)
#         if not buffer:
#             break
#
#         f.write(buffer)
#     f.close()
#     print ("Sucessful to download" + " " + file_name)
#
#
#  getFile(url)