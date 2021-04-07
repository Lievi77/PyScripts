# Author: Shize Li

import pandas

# We are only staging dates in 2020
start_date = pandas.Timestamp('2020-1-1')
end_date = pandas.Timestamp('2020-12-31')

# Holidays
holidays = [
    pandas.Timestamp('2020-1-1'),
    pandas.Timestamp('2020-2-14'),
    pandas.Timestamp('2020-3-17'),
    pandas.Timestamp('2020-4-10'),
    pandas.Timestamp('2020-5-10'),
    pandas.Timestamp('2020-5-18'),
    pandas.Timestamp('2020-6-21'),
    pandas.Timestamp('2020-7-1'),
    pandas.Timestamp('2020-9-7'),
    pandas.Timestamp('2020-10-12'),
    pandas.Timestamp('2020-10-31'),
    pandas.Timestamp('2020-11-11'),
    pandas.Timestamp('2020-12-24'),
    pandas.Timestamp('2020-12-25'),
    pandas.Timestamp('2020-12-26'),
    pandas.Timestamp('2020-12-31'),
]

# Seasons
start_of_spring = pandas.Timestamp('2020-3-19')
start_of_summer = pandas.Timestamp('2020-6-20')
start_of_fall = pandas.Timestamp('2020-9-22')
start_of_winter = pandas.Timestamp('2020-12-21')

# Create table skeleton
table = {
    'day': [],
    'month': [],
    'day_of_week': [],
    'week_in_year': [],
    'is_weekend': [],
    'is_holiday': [],
    'season': [],
    'complete_date': []
}

# Fill table
one_day = pandas.Timedelta(1, 'day')
curr_day = start_date
while (curr_day <= end_date):
    table['day'].append(curr_day.day)
    table['month'].append(curr_day.month)
    table['day_of_week'].append(curr_day.day_of_week + 1)
    table['week_in_year'].append(curr_day.week)
    table['is_weekend'].append(curr_day.day_of_week in [5, 6])
    table['is_holiday'].append(curr_day in holidays)
    table['season'].append(
        "winter" if curr_day < start_of_spring else
        "spring" if curr_day < start_of_summer else
        "summer" if curr_day < start_of_fall else
        "fall" if curr_day < start_of_winter else
        "winter"
    )
    table['complete_date'].append(curr_day)
    curr_day += one_day

# Output
data = pandas.DataFrame(table)
data.to_csv("date_dim.csv", index_label="date_key")
