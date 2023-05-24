import datetime

bdays = [
    datetime.date(1990, 4, 15),
    datetime.date(1985, 6, 20),
    datetime.date(1987, 11, 3),
    datetime.date(1995, 1, 10),
    datetime.date(1993, 9, 30)
]
for year in range(2000, 2011, 5):
    print(f'\nIn {year}:')
    for bday in bdays:
        bday_this_year = datetime.date(bday.year, bday.month, bday.day)
        weekday_name = bday_this_year.strftime('%A')
        print(f"Friend's birthday on {bday_this_year} is on a {weekday_name}")