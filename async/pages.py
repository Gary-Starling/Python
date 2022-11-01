import asyncio
from time import time

async def put(url):
    print("put quer to", url)
    await asyncio.sleep(1)

async def get_data(url):
    print("get data from", url)
    await asyncio.sleep(1)


async def get_all(url):
    await put(url)
    await get_data(url)



lst_func = [
    asyncio.ensure_future(get_all("ya.ru")),
    asyncio.ensure_future(get_all("ozone.com")),
    asyncio.ensure_future(get_all("apple.com"))
]


start_time = time()
print("async execut start")
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*lst_func))
event_loop.close()
print("async execut stop")
print("{:.2F}".format(time() - start_time))