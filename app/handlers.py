import datetime


from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
import app.database.requests as rq

router = Router()

poo = 'Данные еще не записанны'
food = 'Данные еще не записанны'

vitamin_d = 'Витамин D сегодня не принимали!'
iodine = 'Йод сегодня не принимали!'

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'Добро пожаловать! {message.from_user.first_name}', reply_markup=kb.main)

    
@router.message(F.text == 'Записать время')
async def write_data(message: Message):
    await message.answer('Записываю', reply_markup=kb.questions)
 
    
@router.message(F.text == 'Когда кушал?')
async def food_time(message: Message):
    await message.answer(f'{food}') 
 
    
@router.message(F.text == 'Когда какал?')
async def food_time(message: Message):
    await message.answer(f'{poo}')  
 
    
@router.message(F.text == 'Давали витамин D?')
async def food_time(message: Message):
    await message.answer(f'{vitamin_d}')
 
    
@router.message(F.text == 'Давали Йод?')
async def food_time(message: Message):
    await message.answer(f'{iodine}')            

    
@router.callback_query(F.data == 'food')
async def write_food(callback: CallbackQuery):
    timer = str(datetime.datetime.now())
    await rq.set_food_time(timer)
    await callback.message.answer('Записал') 
           
    
@router.callback_query(F.data == 'pooped')
async def write_food(callback: CallbackQuery):   
    await callback.message.answer('Записал')
    global poo   
    poo = f'{datetime.date.today().day} числа'

    
@router.callback_query(F.data == 'vita_D')
async def write_food(callback: CallbackQuery):
    await callback.message.answer('Записал') 
    global vitamin_d
    vitamin_d = 'Да, витамин D сегодня принимали!' 

    
@router.callback_query(F.data == 'iodine')
async def write_food(callback: CallbackQuery):
    await callback.message.answer('Записал') 
    global iodine
    iodine = 'Да, Йод сегодня принимали!'                   