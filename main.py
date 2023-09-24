from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees
from application.newpackage import example_emoji

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    example_emoji()