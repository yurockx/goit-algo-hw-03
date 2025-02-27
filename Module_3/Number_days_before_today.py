from datetime import datetime
def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        return (date.today() - date).days
    except ValueError:
        return "Invalid date format! Please enter the date in the following format: YYYY-MM-DD"