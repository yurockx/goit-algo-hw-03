from datetime import datetime, date
today = date.today()
def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    return (today - date).days