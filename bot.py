from aiogram import Bot, Dispatcher, executor, types
import parser

API_TOKEN = '6595511916:AAHDaRs0nrObNHJBIFRFFf-TAmpMMR_Jn_E'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Введите команду /weather чтобы получить прогноз на сегодня")


@dp.message_handler(commands=['weather'])
async def start(message: types.Message):
    await message.reply("Введите название города на английском: ")


@dp.message_handler()
async def answer(message: types.Message):
    p = parser.Parser(message.text)
    result = p.get_weather()
    await message.answer(result)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)