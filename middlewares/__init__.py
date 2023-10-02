from aiogram import Dispatcher
from middlewares.exists_user import ExistsUserMiddleware

# Подключение мидлвара
def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(ExistsUserMiddleware())
