from unittest import IsolatedAsyncioTestCase, TestCase

from datetime import datetime
from utils import convert_to_iso, get_all_dates

class TestDateList(IsolatedAsyncioTestCase):
    async def test_hour(self):
        dt_from = datetime(2012, 1, 1, 0, 0)
        dt_upto = datetime(2012, 1, 2, 0, 0)
        group_type = 'hour'
        result = await get_all_dates(dt_from, dt_upto, group_type)
        self.assertEqual(len(result), 25)

    async def test_day(self):
        dt_from = datetime(2012, 1, 1)
        dt_upto = datetime(2012, 1, 5)
        group_type = 'day'
        result = await get_all_dates(dt_from, dt_upto, group_type)
        self.assertEqual(len(result), 5)

    async def test_week(self):
        dt_from = datetime(2012, 1, 1)
        dt_upto = datetime(2012, 1, 14)
        group_type = 'week'
        result = await get_all_dates(dt_from, dt_upto, group_type)
        self.assertEqual(len(result), 2)

    async def test_month(self):
        dt_from = datetime(2012, 1, 1)
        dt_upto = datetime(2013, 1, 1)
        group_type = 'month'
        result = await get_all_dates(dt_from, dt_upto, group_type)
        self.assertEqual(len(result), 13)

class TestConvertToISO(TestCase):
    def test_day(self):
        data = '2000-11-14'
        format = '%Y-%m-%d'
        result = convert_to_iso(data, format)
        self.assertEqual(result, '2000-11-14T00:00:00')
