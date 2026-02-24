from datetime import datetime, timedelta, date

def subtract_five_days():
    current_date = datetime.now()
    five_days_ago = current_date - timedelta(days=5)
    print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))

def print_yesterday_today_tomorrow():
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)

def drop_microseconds():
    current_datetime = datetime.now()
    without_microseconds = current_datetime.replace(microsecond=0)
    print("Without microseconds:", without_microseconds)

def calculate_date_difference_seconds():
    date1 = datetime(2024, 1, 1, 12, 0, 0)
    date2 = datetime(2024, 1, 4, 12, 0, 0)
    difference_seconds = (date2 - date1).total_seconds()
    print("Difference in seconds:", difference_seconds)

subtract_five_days()
print_yesterday_today_tomorrow()
drop_microseconds()
calculate_date_difference_seconds()