from dateutil.rrule import rrule, MONTHLY, DAILY, WEEKLY, HOURLY


WRONG_DATA_MESSAGE = (
    'Допустимо отправлять только следующие запросы:\n'
    '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}\n'
    '{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}\n'
    '{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}'
)

GROUP_DATE = {
    'hour': {'format': '%Y-%m-%dT%H', 'type': HOURLY},
    'day': {'format': '%Y-%m-%d', 'type': DAILY},
    'week': {'format': '%Y-%U', 'type': WEEKLY},
    'month': {'format': '%Y-%m', 'type': MONTHLY}
}
