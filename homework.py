from typing import Optional, List
import datetime as dt

DATE_FORMAT = "%d.%m.%Y"
DATE_TODAY = dt.date.today()


class Record:
    def __init__(self, amount: float,
                 comment: str, date: Optional[str] = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = DATE_TODAY
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
                          if x.date == DATE_TODAY])
        return today_count

    def get_week_stats(self) -> float:
        today = DATE_TODAY
        week_ago = today - dt.timedelta(weeks=1)
        week_count = sum([x.amount for x in self.records if x.date <= today
                          and x.date >= week_ago])
        return week_count

    def get_balance(self) -> float:
        remain = self.get_today_stats()
        remain = self.limit - remain
        return remain


class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 73.33
    EURO_RATE = 87.7

    def get_today_cash_remained(self, currency_code: str) -> str:
        currency = {
            'rub': ('руб', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)}
        try:
            value_currency = currency[currency_code][1]
            type_currency = currency[currency_code][0]
        except KeyError:
            print("Убедитесь в правильности ввода валюты")
            exit()
        cash_today = self.get_balance()
        remain = abs(round(cash_today / value_currency, 2))
        if cash_today < 0:
            return ('Денег нет, держись: '
                    f'твой долг - {remain} '
                    f'{type_currency}')
        if cash_today > 0:
            return ('На сегодня осталось '
                    f'{remain} '
                    f'{type_currency}')
        return 'Денег нет, держись'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        today = self.get_today_stats()
        if today < self.limit:
            remain = self.get_balance()
            return ('Сегодня можно съесть что-нибудь ещё,'
                    ' но с общей калорийностью не более '
                    f'{remain} кКал')
        return 'Хватит есть!'
