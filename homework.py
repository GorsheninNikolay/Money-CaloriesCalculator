import datetime as dt

DATE_FORMAT = "%d.%m.%Y"


class Record:
    def __init__(self, amount: float, comment: str, date: str = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()


class Calculator:
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, new_record: Record) -> None:
        self.records.append(new_record)

    def get_today_stats(self) -> float:
        TODAY = 0
        for record in self.records:
            if record.date == dt.date.today():
                TODAY += record.amount
        return TODAY

    def get_week_stats(self) -> float:
        WEEK_COUNT = 0
        for record in self.records:
            days = dt.date.today() - record.date
            if days <= dt.timedelta(days=7) and days >= dt.timedelta(days=0):
                WEEK_COUNT += record.amount
        return WEEK_COUNT


class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 73.33
    EURO_RATE = 87.7

    def get_today_cash_remained(self, currency_code: str) -> str:
        CASH_TODAY = super().get_today_stats()
        currency = {'rub': self.RUB_RATE,
                    'usd': self.USD_RATE,
                    'eur': self.EURO_RATE}
        type_currency = {'rub': 'руб',
                         'usd': 'USD',
                         'eur': 'Euro'}
        if CASH_TODAY == self.limit:
            return 'Денег нет, держись'
        elif CASH_TODAY > self.limit:
            REMAIN = CASH_TODAY - self.limit
            REMAIN = round(REMAIN / currency[currency_code], 2)
            return ('Денег нет, держись: '
                    f'твой долг - {REMAIN} '
                    f'{type_currency[currency_code]}')
        else:
            REMAIN = self.limit - CASH_TODAY
            REMAIN = round(REMAIN / currency[currency_code], 2)
            return ('На сегодня осталось '
                    f'{REMAIN} '
                    f'{type_currency[currency_code]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        TODAY = super().get_today_stats()
        if TODAY < self.limit:
            REMAIN = self.limit - TODAY
            return ('Сегодня можно съесть что-нибудь ещё,'
                    ' но с общей калорийностью не более '
                    f'{REMAIN} кКал')
        if TODAY >= self.limit:
            return 'Хватит есть!'
