import asyncio
from aiogram import Router,F
from aiogram.types import Message,ReplyKeyboardMarkup, KeyboardButton
import random
from aiogram.filters import Command
router = Router()

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="О боте")],
            [KeyboardButton(text="Кинуть кубик")],
        ], resize_keyboard=True
    )
    return keyboard

@router.message(Command(commands=["start"]))
@router.message(F.text.lower() == "о боте")
async def start_command(message:Message):
    await message.answer("Привет, я бот, который умеет кидать кубик от 1 до 6, чтобы кинуть кубик напиши /throwthedice или нажми на кнопку ниже", reply_markup=get_keyboard())
    
    
@router.message(Command(commands=["throwthedice"]))
@router.message(F.text.lower() == "кинуть кубик")
async def throw_the_dice(message: Message):
    q= str(random.randint(1,6))
    msg = await message.answer("кидаю кубик...")
    if q == "1":
        await asyncio.sleep(1)
        await message.answer_photo(photo="https://i.postimg.cc/Jn6S6WNk/qweqwe1.png")
        await msg.delete()
        await message.answer("Кинул кубик и выпало число: " + "<b>" + q + "</b>", parse_mode="HTML", reply_markup=get_keyboard())
    elif q == "2":
        await asyncio.sleep(1)
        await message.answer_photo(photo="https://i.postimg.cc/15NbH2fN/qweqwe2.png")
        await msg.delete()
        await message.answer("Кинул кубик и выпало число: " + "<b>" + q + "</b>", parse_mode="HTML", reply_markup=get_keyboard())
    elif q == "3":
        await asyncio.sleep(1)
        await message.answer_photo(photo="https://i.postimg.cc/fT01KpJ1/qweqwe3.png")
        await msg.delete()
        await message.answer("Кинул кубик и выпало число: " + "<b>" + q + "</b>", parse_mode="HTML", reply_markup=get_keyboard())
    elif q == "4":
        await asyncio.sleep(1)
        await message.answer_photo(photo="https://i.postimg.cc/x1DhF5mC/qweqwe4.png")
        await msg.delete()
        await message.answer("Кинул кубик и выпало число: " + "<b>" + q + "</b>", parse_mode="HTML", reply_markup=get_keyboard())
    elif q == "5":
        await asyncio.sleep(1)
        await message.answer_photo(photo="https://i.postimg.cc/jSHmVf6P/qweqwe5.png")
        await msg.delete()
        await message.answer("Кинул кубик и выпало число: " + "<b>" + q + "</b>", parse_mode="HTML", reply_markup=get_keyboard())
    elif q == "6":
        await asyncio.sleep(1)
        await message.answer_photo(photo="https://i.postimg.cc/R0v8v0G1/qweqwe6.png")
        await msg.delete()
        await message.answer("Кинул кубик и выпало число: " + "<b>" + q + "</b>", parse_mode="HTML", reply_markup=get_keyboard())
    