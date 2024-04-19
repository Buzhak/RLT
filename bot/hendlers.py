import json
from datetime import datetime
from functools import reduce

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from constats import WRONG_DATA_MESSAGE, GROUP_DATE
from main import coll
from utils import convert_to_iso, get_all_dates

router = Router()


@router.message(CommandStart())
async def start_hendler(message: Message) -> None:
    await message.answer('Hello!')


@router.message(F.text.regexp('^\{(.|\n)*\}$'))
async def json_hendler(message: Message) -> None:
    try:
        # Преобразование json в словарь
        data = json.loads(message.text)

        dt_from = datetime.fromisoformat(data['dt_from'])
        dt_upto = datetime.fromisoformat(data['dt_upto'])
        group_type = data['group_type']

        # Формирование запроса к базе
        query = {
            'dt': {
                '$gte': dt_from, '$lte': dt_upto
            }
        }
        group = {
            '_id': {
                '$dateToString': {
                    'format': GROUP_DATE[group_type]['format'],
                    'date': '$dt'
                }
            },
            'count': {
                '$sum': '$value'
            },
        }
        sort = {'_id': 1}

        # Запрос к базе
        res = coll.aggregate([
            {'$match':query},
            {'$group': group},
            {'$sort': sort},
        ])
        res = await res.to_list(length=1000)

        # Формирую данные из бд в словарь
        res_dict = {i['_id']: i['count'] for i in res}
        result_dates_list = res_dict.keys()

        # Формируем список дат диапазне указанном пользователем
        all_dates = await get_all_dates(dt_from, dt_upto, group_type)
        
        # Формируем результат на основе данных из бд и списка дат 
        def process_dates(acc: dict, item: str):
            date = convert_to_iso(item, GROUP_DATE[group_type]['format'])
            acc['labels'].append(date)
            if item in result_dates_list:
                num = int(res_dict[item])
                acc['dataset'].append(num)
            else:
                acc['dataset'].append(0)
            return acc
        data_accumulator = {'dataset': [], 'labels': []}
        reduce(process_dates, all_dates, data_accumulator)

        data = json.dumps(data_accumulator)
    except:
        data = WRONG_DATA_MESSAGE

    await message.answer(str(data))
