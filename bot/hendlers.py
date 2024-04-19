import json
from datetime import datetime

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from constats import WRONG_DATA_MESSAGE, GROUP_DATE

router = Router()


@router.message(CommandStart())
async def start_hendler(message: Message) -> None:
    await message.answer('Hello!')


@router.message(F.text.regexp('^\{(.|\n)*\}$'))
async def json_hendler(message: Message) -> None:
    try:
        data = json.loads(message.text)
        dt_from = datetime.fromisoformat(data['dt_from'])
        dt_upto = datetime.fromisoformat(data['dt_upto'])
        group_type = data['group_type']
        data = f'{GROUP_DATE[group_type]}'
    except:
        data = WRONG_DATA_MESSAGE

    await message.answer(str(data))
