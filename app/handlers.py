from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@router.message(Command("shop"))
async def cmd_shop(message: types.Message):
    await message.answer("Категории")
    
