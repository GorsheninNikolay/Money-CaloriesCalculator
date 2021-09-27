Калькулятор денег и калорий
==

Данный проект предназначен для освоения ООП. Нужно было создать 2 калькулятора - денег и калорий. Они умеют хранить записи (о еде или деньгах), знать дневной лимит (сколько в день можно истратить денег или сколько калорий можно получить) и суммировать записи за конкретные даты.

# О методах

#### Калькулятор денег умеет:

- Сохранять новую запись о расходах методом ```add_record()```
- Считать, сколько денег потрачено сегодня методом ```get_today_stats()```
- Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод ```get_today_cash_remained(currency)```
- Считать, сколько денег потрачено за последние 7 дней — метод ```get_week_stats()```

#### Калькулятор калорий умеет:

- Сохранять новую запись о приёме пищи — метод ```add_record()```
- Считать, сколько калорий уже съедено сегодня — метод ```get_today_stats()```
- Определять, сколько ещё калорий можно/нужно получить сегодня — метод ```get_calories_remained()```
- Считать, сколько калорий получено за последние 7 дней — метод ```get_week_stats()```

# Развертывание проекта

1. Зайдите в GitBash, при необходимости установите
2. При помощи команд 

Перейти в каталог:
```
cd "каталог"
```
Подняться на уровень вверх:
```
cd .. 
```
:exclamation: Перейдите в нужный каталог для клонирования репозитория :exclamation:

3. Клонирование репозитория:
```
git clone https://github.com/GorsheninNikolay/Money-CaloriesCalculator
```
4. Переход в каталог:
```
cd Money-CaloriesCalculator
```
5. Для работы программы нужно ввести соответствующие записи:

### Примеры записей:

##### Для CashCalculator

```Python
r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=1568,
            comment='Наполнение потребительской корзины',
            date='09.03.2019')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')
```
##### Для CaloriesCalculator
```Python
r4 = Record(amount=1186,
            comment='Кусок тортика. И ещё один.',
            date='24.02.2019')
r5 = Record(amount=84, comment='Йогурт.', date='23.02.2019')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019')
```

```Python
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
 ```

6. Запуск проекта:
```
python homework.py
```

И все! :blush:
