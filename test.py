from typing import List, Union, Any
import datetime as dt

print()
print('================================================================================================================')
date_format = '%d.%m.%Y'                # Date format
date_now = dt.datetime.utcnow()         # Date now

class Calculator:
    def __init__(self, limit: Union[int, float]) -> None:
        self.limit = limit              # Limit of cash or calories
        self.records: List[Any] = []
        self.count = 0
        self.week_count = 0
        self.days = 0
        self.week = dt.timedelta(days = 7)
        self.zero = dt.timedelta(days = 0)

    def add_record(self, Record):
        self.records.append(Record)
        self.date_now = date_now.date()
        self.days = self.date_now - Record.date

    def get_today_stats(self):
        for record in self.records:
            if self.days > self.zero:
                if record.date == self.date_now:
                    self.count += record.amount
        if self.count < self.limit:
            return f'Осталось: {self.count}'
        else:
            return f'Превышен лимит'

    def get_week_stats(self):
        for record in self.records:
            if self.days > self.zero:
                if (self.date_now - record.date) <= self.week:
                    self.week_count += record.amount
        return f'{self.week_count}'

class Record:
    def __init__(self, amount: Union[int, float], comment: str, date: Union[str, dt.datetime] = None) -> None:
        self.amount = amount                                    # The variable amount
        self.comment = comment                                  # Comment with buying
        self.date = date                                        # The date of buying
        if self.date == None:                                   # If date is not in the argument, then date is date now
            self.date = date_now.date()
        else:                                                   # If date is the argument, then convert it in the special format
            self.date = dt.datetime.strptime(date, date_format)
            self.date = self.date.date()

    def __str__(self):
        return f'Стоимость: {self.amount}, Комментарий: {self.comment}, Дата: {self.date}'


class CashCalculator(Calculator):
    def __init__(self, limit: Union[int, float], records: List[Any] = []) -> None:
        super().__init__(limit)
        self.money = 0                          # The variable for count expensive
        self.records: List[Any] = []            # Create list for records
        self.week_expenses = 0                  # Creating the variable for couting money for the week
        self.days = 0                           # Createing the variable for defining numbers of days
        self.week = dt.timedelta(days = 7)      # Creating the variable for the limit days
        self.money_week = 0                     # Creating the variable for couting money for the week
    
    USD_RATE = 73.33                   # Course by USD on 13.03.2021
    EURO_RATE = 87.7                   # Course by EURO on 13.03.2021

    def add_record(self, Record):
        self.records.append(Record)                 # Adding the record in the list
        self.date_now = date_now.date()             # Correct the variable date_now in the format of date()
        if self.date_now == Record.date:
            self.money += Record.amount               # Counting expensive and saving in the variable
        self.days = self.date_now - Record.date     # Calculating days
        if self.days <= self.week:                  # If days < 7 then couting our money
            self.money_week += Record.amount
    
    def get_today_cash_remained(self, currency: str) -> Any:
        if currency == "rub":                                                   # If the entered course is ruble
            if self.money == self.limit:                                          # if the expenses = our limit           
                return 'Денег нет, держись'
            elif self.money > self.limit:                                         # If the expenses of money > our limit
                remain = self.money - self.limit                                  # We are counting the debt of money
                return f'Денег нет, держись: твой долг - {remain} руб'
            else:                                                               # If the expenses of money < our limit
                remain = self.limit - self.money                                  # We are counting remains of money
                return f'На сегодня осталось {round(remain, 2)} руб'

        elif currency == "usd":                                                 # If the entered course is usd
            if self.money / self.USD_RATE == self.limit / self.USD_RATE:          # If the expenses = our limit
                return 'Денег нет, держись'
            elif self.money / self.USD_RATE > self.limit / self.USD_RATE:         # If the expenses of money < our limit
                remain = self.money / self.USD_RATE - self.limit / self.USD_RATE  # We are counting the debt of money
                return f'Денег нет, держись: твой долг - {round(remain, 2)} USD'
            else:                                                               # If the expenses of money < our limit
                remain = self.limit / self.USD_RATE - self.money / self.USD_RATE  # We are counting remains of money
                return f'На сегодня осталось {round(remain, 2)} USD'
        
        elif currency == "eur":                                                 # If the entered course is eur
            if self.money / self.EURO_RATE == self.limit / self.EURO_RATE:        # We are counting remains of money
                return 'Денег нет, держись'
            elif self.money / self.EURO_RATE > self.limit / self.EURO_RATE:       # If the expenses of money > our limit
                remain = self.money / self.EURO_RATE - self.limit / self.EURO_RATE    # We are counting the debt of money
                return f'Денег нет, держись: твой долг - {round(remain, 2)} Euro'
            else:                                                               # If the expenses of money < our limit
                remain = self.limit / self.EURO_RATE - self.money / self.EURO_RATE    # We are counting remains of money
                return f'На сегодня осталось {round(remain, 2)} Euro'

    def get_week_stats(self) -> str:                                                   # Remaining of money for week
        return(f'Денег потрачено за последние 7 дней: {self.money_week}')

    def print_records(self) -> Any:                                                           # Print our records
        print()
        print('////////////////////////////////////////////Cash////////////////////////////////////////////////////////////////')
        print('Все покупки:')
        for record in self.records:
            print(record)
        return '////////////////////////////////////////////////////////////////////////////////////////////////////////////////'



class CaloriesCalculator(Calculator):
    def __init__(self, limit: Union[int, float], records: List[Any] = []) -> None:
        super().__init__(limit)
        self.records: List[Any] = []            # Creating list for records
        self.calories = 0                       # Creating variable for counting calories
        self.calories_week = 0                  # Creating variable for counting calories for week   
        self.days = 0                           # Creating variable 'days' for counting days
        self.week = dt.timedelta(days = 7)      # Creating the variable for the limit days

    def add_record(self, Record):
        self.records.append(Record)             # Add the record
        self.date_now = date_now.date()         # Convert date now in the format date()
        if Record.date == self.date_now:        # If date in record == date now, then counting...
            self.calories += Record.amount
        self.days = self.date_now - Record.date # Counting days of eating
        if self.days <= self.week:              # If days <= 7 and > 0, then counting calories
            self.calories_week += Record.amount

    def get_today_stats(self) -> Any:
        return f'Сегодня съедено {self.calories} калорий'


    def get_calories_remained(self) -> Any:
        if self.calories <= self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.calories} кКал'

        elif self.calories > self.limit:
            return 'Хватит есть!'

    def get_week_stats(self) -> Any:
        return f'За последние 7 дней получено: {self.calories_week} калорий'

    def print_records(self) -> Any:
        print()
        print('///////////////////////////////////////////Calories/////////////////////////////////////////////////////////////')
        print('Все покупки:')
        for record in self.records:
            print(record)
        return '////////////////////////////////////////////////////////////////////////////////////////////////////////////////'



cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(3000)
r1 = Record(amount=145, comment='Безудержный шопинг', date='06.03.2019')
r2 = Record(amount=400, comment='Отель')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2021')
r4 = Record(amount=1186,
            comment='Кусок тортика. И ещё один...',
            date='24.02.2019')
r5 = Record(amount=8400, comment='Йогурт', date='23.02.2019')
r6 = Record(amount=1140, comment='Баночка чипсов.') 
r7 = Record(amount=1500, comment='Чизбургер') 
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)
calories_calculator.add_record(r4)
calories_calculator.add_record(r5)
calories_calculator.add_record(r6)
calories_calculator.add_record(r7)

print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_week_stats())
print(cash_calculator.print_records())
print()
print(calories_calculator.get_today_stats())
print(calories_calculator.get_calories_remained())
print(calories_calculator.get_week_stats())
print(calories_calculator.print_records())
print('================================================================================================================')
print()