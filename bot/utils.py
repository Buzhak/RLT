from datetime import datetime
from dateutil.rrule import rrule

from constats import GROUP_DATE


async def get_all_dates(
    dt_from: datetime, dt_upto: datetime, group_type: str
) -> list[str]:
    '''
    Функция получает два datetime (dt_from, dt_upto) между которыми нужно найти все
    часы|дни|недели|месяцы (group_type) и вернуть стоковый список с их обозначениями.
    '''
    all_dates = [
        dt.strftime(
            GROUP_DATE[group_type]['format']
        ) for dt in rrule(
            GROUP_DATE[group_type]['type'], dtstart=dt_from, until=dt_upto
        )
    ]
    return all_dates


def convert_to_iso(date: str, format: str) -> str:
    '''
    Функция получает стоковое представление даты "2000-10"
    формат этой даты "%Y-%m", преобразует дату в формат "%Y-%m-%dT%H:%M:%S"
    и возвращает её.
    '''
    iso_date_str = datetime.strptime(date, format).strftime('%Y-%m-%dT%H:%M:%S')
    return iso_date_str
