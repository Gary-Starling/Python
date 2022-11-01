from time import sleep, time
import asyncio


def usual_func(name):
    for i in range(1, 4, 1):
        print("measurments", i, ":", name)
        sleep(1)


async def async_function(name):
    for i in range(1, 4, 1):
        print("measurments", i, ":", name)
        await asyncio.sleep(1)

def callback(name):
    print(name)

if __name__ == "__main__":

    lst_func = [
        asyncio.ensure_future(async_function("cor A")),
        asyncio.ensure_future(async_function("cor B")),
        asyncio.ensure_future(async_function("cor C"))
    ]
    '''
    start_time = time()
    print("usual execut start")
    usual_func("func A")
    usual_func("func B")
    usual_func("func C")
    print("usual execut stop")
    print("{:.2F}".format(time() - start_time))
    '''

    start_time = time()
    print("async execut start")
    event_loop = asyncio.get_event_loop()
    event_loop.call_soon(callback, "call soon func 1")
    event_loop.call_later(2,callback, "call soon func 2")
    event_loop.run_until_complete(asyncio.gather(*lst_func))
    event_loop.close()
    print("async execut stop")
    print("{:.2F}".format(time() - start_time))
    print('///')
