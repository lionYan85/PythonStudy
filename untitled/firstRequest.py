import requests  # 导入爬虫的库，不然调用不了爬虫的函数


class firstRequest():

    def requestBD():
        response = requests.get("http://www.baidu.com")  # 生成一个response对象

        response.encoding = response.apparent_encoding  # 设置编码格式

        print("状态码:" + str(response.status_code))  # 打印状态码

        print(response.text)  # 输出爬取的信息

        file = open("E:\\爬虫\\baidu.html", "w", encoding="utf")  # 打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制

        file.write(response.text)

        file.close()

    def postRequest():
        data = {
            "name": "hezhi",
            "age": 20
        }
        response = requests.post("http://httpbin.org/post", params=data)  # post传参
        print(response.status_code)  # 状态码
        print(response.text)

    def requestZH():
        # response = requests.get("http://www.zhihu.com")  # 第一次访问知乎，不设置头部信息
        #
        # print("第一次,不设头部信息,状态码:" + response.status_code)  # 没写headers，不能正常爬取，状态码不是 200

        # 下面是可以正常爬取的区别，更改了User - Agent字段

        headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"

        }  # 设置头部信息,伪装浏览器

        response = requests.get("http://www.zhihu.com", headers=headers)  # get方法访问,传入headers参数，

        print(response.status_code)  # 200！访问成功的状态码

        print(response.text)

    def getImage():
        response = requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")  # get方法的到图片响应

        file = open("E:\\爬虫\\baidu_logo.gif", "wb")  # 打开一个文件,wb表示以二进制格式打开一个文件只用于写入

        file.write(response.content)  # 写入文件

        file.close()  # 关闭操作，运行完毕后去你的目录看一眼有没有保存成功

    # requestBD()
    requestZH()
    # getImage()
