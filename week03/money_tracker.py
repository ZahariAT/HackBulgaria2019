import sys
#work with dictionaries

def list_user_data(all_user_data):
    with open(all_user_data, 'r') as f:
        return f.read()


def show_user_incomes(all_user_data):
    pass


def show_user_savings(all_user_data):
    pass


def show_user_deposits(all_user_data):
    pass


def show_user_expenses(all_user_data):
    pass


def list_user_expenses_ordered_by_categories(all_user_data):
    pass


def show_user_data_per_date(date, all_user_data):
    pass


def list_income_categories(all_user_data):
    pass


def list_expense_categories(all_user_data):
    pass


def add_income(income_category, money, date, all_user_data):
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass

def main():
    print(list(list_user_data(sys.argv[1])))

if __name__ == '__main__':
    main()