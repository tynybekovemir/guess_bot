from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_keyboards = [
    KeyboardButton('MBANK и полезные ссылки'),
    KeyboardButton('SWIFT перевод'),
    KeyboardButton('Кредит'),
    KeyboardButton('Депозиты'),
    KeyboardButton('ОТДЕЛЕНИЯ И ФИЛИАЛЫ'),
    KeyboardButton('КАРТА БАНКОМАТОВ'),
    KeyboardButton('MBusiness'),
    KeyboardButton('Связаться с оператором'),
]
start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(text=['2', 'SWIFT перевод']) 
async def swift_transfer(message:types.Message):  
    await message.answer("Здесь будет информация о SWIFT переводах.")
    
@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"""ЭСКЕРТҮҮ! Урматтуу {message.from_user.full_name}, шылуундардан сак болуңуз!
Белгисиз шилтемелерди ээрчибеңиз жана картаңыздын маалыматын киргизбеңиз.
Сиздин эсебиңизден акча каражатын алдоо жолу менен чыгарып салуу коркунучун болтурбоо үчүн төлөмдүн ырастоочу коддорун үчүнчү жактар менен бөлүшпөңүз!

Саламатсызбы! Сизди "MBANK"- тын кардарларды колдоо кызматы кабыл алат. Биздин адистер баардык суроолоруңузга кезеги менен жооп беришет.

Тейлөө тилин тандаңыз

ВНИМАНИЕ! Уважаемый клиент, остерегайтесь действий мошенников! 
Не переходите по неизвестным ссылкам и не вводите данные своей карты.
Не передавайте коды подтверждения для оплаты третьим лицам во избежание рисков мошеннического списания денежных средств с Вашего счета! 

Здравствуйте, Вас приветствует служба поддержки клиентов "MBANK". Наши специалисты ответят на все Ваши вопросы в порядке очереди.

🔹 1 - MBANK и полезные ссылки
🔹 2 - SWIFT перевод
🔹 3 - Платежные карты
🔹 4 - Кредит
🔹 5 - Депозиты
🔹 6 - ОТДЕЛЕНИЯ И ФИЛИАЛЫ
🔹 7 - КАРТА БАНКОМАТОВ
🔹 8 - MBusiness
🔹 9 - Связаться с оператором""", reply_markup=start_button)

@dp.message_handler(text=['1', 'MBANK и полезные ссылки'])
async def mbank_urls(message:types.Message):
    await message.answer("""Карту нашего Банка можно пополнить через следующие платежные терминалы:                                                                                                               
   "Оңой "
   "Айыл Банк"
   "Pay24"
   "Quick Pay"
    "UMAI"                                                                                               
Пополнение через платежные терминалы и электронные кошельки БЕСПЛАТНО до 100000 сомов в месяц. Свыше будет взыматься комиссия 1% от суммы пополнения.
      
   2. Из списка выбираем «Банковские услуги» и далее ➡️ «MBANK».

   3. Вводим номер телефона, подключенный к MBANK, в формате 996*** .

   4. Проверяем введенный номер телефона и ФИО получателя.

   5. Вводим необходимую сумму и завершаем пополнение.""")

executor.start_polling(dp)