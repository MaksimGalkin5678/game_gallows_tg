from aiogram import Bot,Dispatcher,executor
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from middlewares import setup_middlewares
from sql import create_dbx

loop = asyncio.new_event_loop()
bot = Bot(token,parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot,loop=loop,storage=storage)

async def shutdown(dp):
    await storage.close()
    await bot.close()

#Запуск бота 
if __name__ == '__main__':
    print("Бот запустился")
    from handlers import *
    create_dbx() #Проверяем есть ли БД или создаем ее
    setup_middlewares(dp) #Подключаем мидлвар, чтобы не падал бот
    executor.start_polling(dp,  on_shutdown=shutdown)

