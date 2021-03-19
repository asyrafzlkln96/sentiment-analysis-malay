#!/usr/local/bin/python3.5
#=========Get asyncio =========
import asyncio
import aiohttp
from aiohttp import ClientSession
import datetime

# start = datetime.datetime()

async def retrieveInfo(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json ={
        "RequestHeader": {
        "EventName": "evRetrieveDB",
        "DateTimeSend": "30/10/2018 14:39:48",
        "AccNo": "1032914549",
        "IntentCode": "1"
        }
        }) as response:
            response = await response.read()
            print(response)
            # print(response.status_code)

            # await session.post(url, json={'example': 'text'})

loop = asyncio.get_event_loop()

loop.run_until_complete(retrieveInfo("http://127.0.0.1:8000/api/spice/retrieveDB"))

# end = datetime.datetime()

# fin = start - end
# print(fin) 


# import asyncio
# import aiohttp


# # async def make_numbers(numbers, _numbers):
# #     for i in range(numbers, _numbers):
# #         yield i

# async def retrieveInfo():
#    url = "http://127.0.0.1:8000/"
#    async with aiohttp.ClientSession() as session:

#     async with session.post(url, data ={
#     "RequestHeader": {
#     "EventName": "evRetrieveDB",
#     "DateTimeSend": "30/10/2018 14:39:48",
#     "AccNo": "1032914549",
#     "IntentCode": "1"
#     }
#     }) as response:
#         data = await response.text()
#     # print("-> Creating account number %d" % x)
#         print(data)

# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(retrieveInfo())
# finally:
#     loop.close()

# import requests_async as requests


#     async with requests.Session() as session:
#         # response = await session.get('https://example.org')
#         response = await requests.post('http://127.0.0.1:8000/api/spice/retrieveDB', data ={
#         "RequestHeader": {
#         "EventName": "evRetrieveDB",
#         "DateTimeSend": "30/10/2018 14:39:48",
#         "AccNo": "1032914549",
#         "IntentCode": "1"
#         }
#         print(response.status_code)
#         print(response.text)