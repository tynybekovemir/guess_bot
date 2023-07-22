from aiogram import Bot, Dispatcher, executor, types
import config
import random

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}\nЯ буду загадывать число, а ты должен угадать \nПоиграем? /go')


random_num = random.randint(1,3)


@dp.message_handler(commands=["go"])
async def go(message: types.Message):
    await message.answer("я загадал число бот  от 1-3")

@dp.message_handler(text = "1")
async def hello(message: types.Message):
    if random_num == 1:
      await message.answer("Поздравляю! вы пошутке отгадали ")
    else:
      await message.answer("ты бот проиграл")
      await message.answer("Еще раз бот ? /go")


@dp.message_handler(text = "2")
async def hello(message: types.Message):
    if random_num == 2:
      await message.answer("Поздравляю! 1-вые жизни ты отгадал")
    else:
      await message.answer("ты бот проиграл ")
      await message.answer("Еще раз бот? /go")
      

@dp.message_handler(text = "3")
async def hello(message: types.Message):
    if random_num == 3:
      await message.answer("Поздравляю! вы отгадали")
    else:
      await message.answer("ты бот ты проиграл")
      await message.answer("Еще раз бот ? /go")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("/start")

executor.start_polling(dp)