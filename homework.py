from typing import Optional, List, Dict, Tuple
import datetime as dt

DATE_FORMAT = "%d.%m.%Y"


class Record:
    def __init__(self, amount: float,
                 comment: str, date: Optional[str] = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()


class Calculator:
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records: List[Record] = []

    def add_record(self, new_record: Record) -> None:
        self.records.append(new_record)

    def get_today_stats(self) -> float:
        today_count = sum([x.amount for x in self.records
                          if x.date == dt.date.today()])
        return today_count

    def get_week_stats(self) -> float:
        today = dt.date.today()
        week_ago = today - dt.timedelta(weeks=1)
        week_count = sum([x.amount for x in self.records if x.date <= today
                          and x.date >= week_ago])
        return week_count

    def count_remain(self) -> float:
        remain = self.get_today_stats()
        remain = abs(remain - self.limit)
        return remain


class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 73.33
    EURO_RATE = 87.7

    def get_today_cash_remained(self, currency_code: str) -> str:
        CASH_TODAY = self.get_today_stats()
        currency: Dict[str, Tuple[str, float]] = {
            'rub': ('руб', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)}
        value_currency = currency[currency_code][1]
        type_currency = currency[currency_code][0]
        if CASH_TODAY > self.limit:
            REMAIN = self.count_remain()
            REMAIN = round(REMAIN / value_currency, 2)
            return ('Денег нет, держись: '
                    f'твой долг - {REMAIN} '
                    f'{type_currency}')
        if CASH_TODAY < self.limit:
            REMAIN = self.count_remain()
            REMAIN = round(REMAIN / value_currency, 2)
            return ('На сегодня осталось '
                    f'{REMAIN} '
                    f'{type_currency}')
        return 'Денег нет, держись'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        TODAY = self.get_today_stats()
        if TODAY < self.limit:
            REMAIN = self.count_remain()
            return ('Сегодня можно съесть что-нибудь ещё,'
                    ' но с общей калорийностью не более '
                    f'{REMAIN} кКал')
        return 'Хватит есть!'
