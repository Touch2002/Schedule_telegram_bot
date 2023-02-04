import datetime as dtime
import pandas as pd
from week_type import weekType


class ScheduleRead:
    def __init__(self):
        self.wt = weekType()
        self.mon = None
        self.tue = None
        self.wed = None
        self.thu = None
        self.fri = None

        read = pd.read_csv('kn_new.csv')

        if self.wt == 'чисельник':
            wt = 1
        else:
            wt = 2
        self.mon = read.values[0][wt].replace('@', '\n')
        self.tue = read.values[1][wt].replace('@', '\n')
        self.wed = read.values[2][wt].replace('@', '\n')
        self.thu = read.values[3][wt].replace('@', '\n')
        self.fri = read.values[4][wt].replace('@', '\n')


class Schedule(ScheduleRead):
    def __init__(self):
        super().__init__()
        self.today = dtime.datetime.today().weekday()

    def schedule_today(self):
        dict_day = {0: self.mon, 1: self.tue, 2: self.wed, 3: self.tue, 4: self.fri}
        if dict_day.get(self.today, False):
            res = dict_day.get(self.today)
        else:
            res = 'На сьогодні розкладу немає'
        return res

    def week_correct(self):
        if not self.wt == weekType():
            ScheduleRead()


s = Schedule().mon
print(s)
