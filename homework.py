from typing import List, Union, Any
import datetime as dt

print()
print('=====================================================================')
date_format = '%d.%m.%Y'                # Date format
date_now = dt.datetime.utcnow()         # Date now


class Calculator:
    def __init__(self, limit: Union[int, float]) -> None:
        self.limit = limit              # Limit of cash or calories
        self.week_count = 0
        self.count = 0
        self.date_now = date_now.date()
        self.records: List[Any] = []

    def add_record(self, Record) -> None:
        self.records.append(Record)
        self.days = date_now.date() - Record.date
        if self.days >= dt.timedelta(days=0):
            if Record.date == self.date_now:
                self.count += Record.amount
                self.week_count += Record.amount
            elif self.days <= dt.timedelta(days=7):
                self.week_count += Record.amount

    def get_today_stats(self) -> Union[int, float]:
        if CaloriesCalculator:
            return self.count
        elif CashCalculator:
            return self.count

    def get_week_stats(self) -> Union[int, float]:
        if CaloriesCalculator:
            return self.week_count
        elif CashCalculator:
            return self.week_count


class Record:
    def __init__(self, amount: float, comment: str, date: Any = None) -> None:
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = date_now.date()
        else:
            self.date = dt.datetime.strptime(date, date_format)
            self.date = self.date.date()

        def __str__(self):
            return self.amount
            return self.comment
            return self.date


class CashCalculator(Calculator):

    USD_RATE = 73.33
    EURO_RATE = 87.7

    def __init__(self, limit: float, records: List[Any] = []) -> None:
        super().__init__(limit)

    def add_record(self, Record):
        return Calculator.add_record(self, Record)

    def get_today_cash_remained(self, currency: str) -> Any:
        if currency == "rub":
            if self.count == self.limit:
                return 'Денег нет, держись'
            elif self.count > self.limit:
                rem = self.count - self.limit
                return f'Денег нет, держись: твой долг - {rem} руб'
            else:
                rem = self.limit - self.count
                return f'На сегодня осталось {round(rem, 2)} руб'

        elif currency == "usd":
            if self.count / self.USD_RATE == self.limit / self.USD_RATE:
                return 'Денег нет, держись'
            elif self.count / self.USD_RATE > self.limit / self.USD_RATE:
                rem = self.count / self.USD_RATE - self.limit / self.USD_RATE
                return f'Денег нет, держись: твой долг - {round(rem, 2)} USD'
            else:
                rem = self.limit / self.USD_RATE - self.count / self.USD_RATE
                return f'На сегодня осталось {round(rem, 2)} USD'

        elif currency == "eur":
            if self.count / self.EURO_RATE == self.limit / self.EURO_RATE:
                return 'Денег нет, держись'
            elif self.count / self.EURO_RATE > self.limit / self.EURO_RATE:
                rem = self.count / self.EURO_RATE - self.limit / self.EURO_RATE
                return f'Денег нет, держись: твой долг - {round(rem, 2)} Euro'
            else:
                rem = self.limit / self.EURO_RATE - self.count / self.EURO_RATE
                return f'На сегодня осталось {round(rem, 2)} Euro'

    def get_today_stats(self) -> Any:
        return f'За сегодня денег потрачено: {self.count}'

    def get_week_stats(self) -> Any:
        return f'За последние 7 дней потрачено денег: {self.week_count}'

    def print_records(self) -> Any:
        print()
        print('///////////////////Cash///////////////////////////////////////')
        print('Все покупки:')
        for record in self.records:
            print(f'Стоимость: {record.amount}; '
                  f'Комментарий: {record.comment}; '
                  f'Дата: {record.date}')
        return '//////////////////////////////////////////////////////////////'


class CaloriesCalculator(Calculator):
    def __init__(self, limit: float, records: List[Any] = []) -> None:
        super().__init__(limit)

    def add_record(self, Record) -> None:
        Calculator.add_record(self, Record)

    def get_today_stats(self) -> Any:
        return f'Сегодня получено {self.count} калорий'

    def get_calories_remained(self) -> Any:
        if self.count <= self.limit:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью не более '
                    f'{self.limit - self.count} кКал')
        elif self.count > self.limit:
            return 'Хватит есть!'

    def get_week_stats(self) -> Any:
        return f'За последние 7 дней получено: {self.week_count} калорий'

    def print_records(self) -> Any:
        print()
        print('//////////////////Calories////////////////////////////////////')
        print('Записи питания:')
        for record in self.records:
            print(f'Количество калорий: {record.amount}; '
                  f'Комментарий: {record.comment}; '
                  f'Дата: {record.date}')
        return '//////////////////////////////////////////////////////////////'


cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(3000)
r1 = Record(amount=145, comment='Безудержный шопинг', date='06.03.2019')
r2 = Record(amount=400, comment='Отель', date='13.03.2021')
r3 = Record(amount=238, comment='Катание на такси')
r4 = Record(amount=1186,
            comment='Кусок тортика. И ещё один...',
            date='24.02.2019')
r5 = Record(amount=840, comment='Йогурт')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='13.03.2021')
r7 = Record(amount=1500, comment='Чизбургер')
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)
calories_calculator.add_record(r4)
calories_calculator.add_record(r5)
calories_calculator.add_record(r6)
calories_calculator.add_record(r7)

print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print(cash_calculator.print_records())
print()
print(calories_calculator.get_today_stats())
print(calories_calculator.get_calories_remained())
print(calories_calculator.get_week_stats())
print(calories_calculator.print_records())
print('=====================================================================')
print()