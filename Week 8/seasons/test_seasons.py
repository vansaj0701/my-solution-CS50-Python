from seasons import Minutes
from datetime import datetime


def test_convert():
    date_object = datetime.strptime("1999-01-01", "%Y-%m-%d").date()
    current_date = datetime.strptime("2000-01-01", "%Y-%m-%d").date()
    minutes = Minutes(date_object, current_date)
    assert str(minutes) == "Five hundred twenty-five thousand, six hundred minutes"
