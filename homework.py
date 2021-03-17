from typing import List, Any
import datetime as dt


class Record:
    def __init__(self, amount: float, comment: str, date: dt.datetime = None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    count = 0
    week_count = 0

    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records: List[Any] = []

    def add_record(self, cls: Record) -> None:
        self.records.append(cls)
        self.days = dt.datetime.today().date() - cls.date
        if self.days >= dt.timedelta(days=0):
            if cls.date == dt.datetime.today().date():
                self.count += cls.amount
                self.week_count += cls.amount
            elif self.days <= dt.timedelta(days=7):
                self.week_count += cls.amount

    def get_today_stats(self) -> float:
        for record in self.records:
            if record.date == dt.datetime.today():
                self.count += record.amount
        return self.count

    def get_week_stats(self) -> float:
        return self.week_count


class CashCalculator(Calculator):
    USD_RATE = 73.33
    EURO_RATE = 87.7

    def get_today_cash_remained(self, type: str) -> Any:
        currency = {'rub': 1,
                    'usd': self.USD_RATE,
                    'eur': self.EURO_RATE}
        type_currency = {'rub': 'руб',
                         'usd': 'USD',
                         'eur': 'Euro'}
        if self.count == self.limit:
            return 'Денег нет, держись'
        elif self.count > self.limit:
            rem = self.count - self.limit
            return (f'Денег нет, держись: '
                    f'твой долг - {round(rem / currency[type], 2)} '
                    f'{type_currency[type]}')
        else:
            rem = self.limit - self.count
            return (f'На сегодня осталось '
                    f'{round(rem / currency[type], 2)} '
                    f'{type_currency[type]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> Any:
        if self.count <= self.limit:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью не более '
                    f'{self.limit - self.count} кКал')
        else:
            return 'Хватит есть!'
