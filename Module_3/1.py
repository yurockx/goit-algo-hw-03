from datetime import datetime, date
#transform string to date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()
#current date
today = date.today()
#function to define the difference from current day
def get_days_from_today(date):
    date = string_to_date(date)
    return (today - date).days
