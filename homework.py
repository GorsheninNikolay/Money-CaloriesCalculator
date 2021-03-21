from typing import Optional, List
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
        today = dt.date.today()
        today_count = sum([x.amount for x in self.records
                          if x.date == today])
        return today_count

    def get_week_stats(self) -> float:
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=6)
        week_count = sum([x.amount for x in self.records
                         if today >= x.date >= week_ago])
        return week_count

    def get_balance(self) -> float:
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 73.33
    EURO_RATE = 87.7

    def get_today_cash_remained(self, currency_code: str) -> str:
        currency = {
            'rub': ('руб', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)}
        if currency_code not in currency:
            raise ValueError("Убедитесь в правильности ввода валюты")
        value_currency = currency[currency_code][1]
        type_currency = currency[currency_code][0]
        cash_today = self.get_balance()
        remain = round(cash_today / value_currency, 2)
        if cash_today == 0:
            return 'Денег нет, держись'
        if cash_today < 0:
            remain = abs(remain)
            return ('Денег нет, держись: '
                    f'твой долг - {remain} '
                    f'{type_currency}')
        return ('На сегодня осталось '
                f'{remain} '
                f'{type_currency}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        remain = self.get_balance()
        if remain > 0:
            return ('Сегодня можно съесть что-нибудь ещё,'
                    ' но с общей калорийностью не более '
                    f'{remain} кКал')
        return 'Хватит есть!'
