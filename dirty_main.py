from datetime import *
from application.db.people import *
from application.newpackage import *
from application.salary import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    example_emoji()