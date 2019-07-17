import requests
import time


class AppTest02:

    def __init__(self):
        pass



    def out_of_memery_simple(self, int):
        url = "http://localhost:8888/gc/outOfMemerySimple/" + str(int)

        payload = "{'id':'11'}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ea5836d6-03d3-43a8-a779-5603128fca38,22705b68-db5f-4ae8-ae9b-1ca079d9a4c9",
            'Host': "localhost:8888",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def add_memery_simple(self, int):
        url = "http://localhost:8888/gc/addMemerySimple/" + str(int)
        payload = "{'id':'11'}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ea5836d6-03d3-43a8-a779-5603128fca38,22705b68-db5f-4ae8-ae9b-1ca079d9a4c9",
            'Host': "localhost:8888",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)

    def out_of_memery(self, int):
        url = "http://localhost:8888/gc/outOfMemery/" + str(int)

        payload = "{'id':'11'}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ea5836d6-03d3-43a8-a779-5603128fca38,22705b68-db5f-4ae8-ae9b-1ca079d9a4c9",
            'Host': "localhost:8888",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def add_memery(self, int):
        url = "http://localhost:8888/gc/addMemery/" + str(int)
        payload = "{'id':'11'}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ea5836d6-03d3-43a8-a779-5603128fca38,22705b68-db5f-4ae8-ae9b-1ca079d9a4c9",
            'Host': "localhost:8888",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)


if __name__ == '__main__':
    for i in range(0, 100000):
        print("Call the interface with id of :"+str(i))
        appTest02 = AppTest02()

        # YGC
        # appTest02.add_memery(i)
        # appTest02.add_memery_simple(i)

        # FGC
        appTest02.out_of_memery_simple(i)

        # FGC but out of memery
        # appTest02.out_of_memery(i)

        # Mix GC
        # if i > 10 and i % 100 == 0:
        #     appTest02.out_of_memery(i)
