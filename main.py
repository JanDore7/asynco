# Корутина работает как генератор acync - явный флаг , что функция является асинхронной (корутиной) await - явный
# флаг, что в этом месте функция встает на паузу и дает работать другим , пока ждет свои данные event loop - цикл
# событий, механизм, который отвечает за планирование и запуск корутин. Можно представить как список\очередь ,
# из которого в вечном цикле достаются и запускаются корутины asyncio.wait(task) необходимо создать список задач
# внутри асинхронной функции. Не останавливает работу если падает корутина  метод asyncio.wait(tasks) предназначен для
# ожидания завершения задач, переданных в него в виде итерируемого объекта (например, списка). Он асинхронно ожидает
# выполнения всех задач (объектов Task или Future), переданных ему, и возвращает пару множеств (set), содержащих
# задачи (Task и Future), которые были выполнены и отменены. При этом asyncio.wait не отменяет задачи самостоятельно;
# если задача была отменена до того, как asyncio.wait завершил ожидание, она будет включена во множество отменённых
# задач.
#
# Возвращаемое значение выглядит так: (done, pending) done: Множество (set) задач, которые были успешно выполнены или
# отменены к моменту завершения ожидания. Это значит, что для каждой задачи в этом множестве метод task.done() вернёт
# True. pending: Множество (set) задач, которые ещё не были выполнены к моменту, когда был превышен таймаут (если он
# указан) или asyncio.wait был отменён. Для задач в этом множестве метод task.done() вернёт False. asyncio.wait
# принимает несколько ключевых аргументов, которые позволяют настроить его поведение, таких как timeout (время
# ожидания в секундах), return_when (условие возврата), что позволяет контролировать, при каком условии asyncio.wait
# вернёт управление вызывающему коду — например, как только любая задача выполнена (FIRST_COMPLETED), все задачи
# выполнены (ALL_COMPLETED) или какая-либо задача отменена (FIRST_EXCEPTION).
#
#-----------------------------------
# asyncio.as_completed(tasks) также список задач создается внутри функции, позволяет обработать каждую корутину
# Задачи возвращаются по мере их выполнения. 


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


async def one(value):
    print('Старт №1')
    await asyncio.sleep(1)
    print('Стоп №1')
    return value * 2


async def two(value):
    print('Старт №2')
    if value != 2:
        await asyncio.sleep(2)
        print('Стоп №2')
        return value * 2
    raise ValueError('Исключение')


async def three(value):
    print('Старт №3')
    await asyncio.sleep(3)
    print('Стоп №3')
    return value * 2





@decor
async def main():
    tasks = [asyncio.create_task(one(10)), asyncio.create_task(two()), asyncio.create_task(three(30))]
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # asyncio.create_task(three())
    # await asyncio.gather(one(), two(), three())
    # a, d = await asyncio.wait(tasks)
    # for i in a:
    #     print(i.result())
    # for task in asyncio.as_completed(tasks):
    #     try:
    #         await task
    #     except ValueError:
    #         print(f'Ошибка в работе функции {task}')
    await asyncio.wait(tasks)
    for i in tasks:
        print(i.result())


if __name__ == '__main__':
    # print(example())
    # print(exemlle_f())

    # 1 ------------------------------------
    asyncio.run(main())
