import datetime

today = datetime.date.today()
birth_date = datetime.date(1985,05,17)

diff = today - birth_date
print diff.days
