import datetime as dtime


def weekType():
    passed_week = 35
    now = dtime.datetime.now().date()
    d = dtime.date(now.year, now.month, now.day)
    f = d.strftime("%W")
    if (int(f) - passed_week) % 2 == 0:
        week_type = 'чисельник'
    else:
        week_type = 'знаменник'
    return week_type