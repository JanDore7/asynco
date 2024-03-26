# Корутина работает как гениратор
# acync - явный флаг , что функция является асинхронной (корутиной)
# await - явный флаг, что в этом месте функция встает на паузу и дает работать другим , пока ждет свои данные
# event loop - цикл событий , механизм, который отвечает за планирование и запуск корутин. Можно представить как
# список\очередь , из которого в вечном цикле достааются и запускаются корутины


import asyncio
import time


# async def example():
#      print(100)
#
#
# def exemlle_f():
#     print(f'Привет я обычная функция')


# 1 ------------------------------------

def decor(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        finish = time.time() - start
        print(finish)
        return result
    return wrapper


async def one():
    print('Старт №1')
    await asyncio.sleep(1)
    print('Стоп №1')

async def two():
    print('Старт №2')
    await asyncio.sleep(2)
    print('Стоп №2')


async def three():
    print('Старт №3')
    await asyncio.sleep(3)
    print('Стоп №3')


@decor
async def main():
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # asyncio.create_task(three())
    await asyncio.gather(one(), two(), three())



if __name__ == '__main__':
    # print(example())
    # print(exemlle_f())

    # 1 ------------------------------------
    asyncio.run(main())
