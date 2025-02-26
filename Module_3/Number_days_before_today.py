from datetime import datetime
def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    return (date.today() - date).days