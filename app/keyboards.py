from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Когда кушал?'),
                                      KeyboardButton(text='Когда какал?')],
                                     [KeyboardButton(text='Давали витамин D?'), 
                                      KeyboardButton(text='Давали Йод?')],
                                     [KeyboardButton(text='Записать время')]],
                           resize_keyboard=True)

questions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Покушал',callback_data='food'), 
     InlineKeyboardButton(text='Покакал', callback_data='pooped')],
    [InlineKeyboardButton(text='Приняли Витамин D', callback_data='vita_D'),
     InlineKeyboardButton(text='Приняли Йод', callback_data='iodine')]])
