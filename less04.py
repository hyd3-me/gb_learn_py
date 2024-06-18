import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

def add_operation(operation_string):
    operations.append(operation_string)
    return 0

def print_not_multiplicity():
    print('Сумма должна быть кратной 50 у.е.')

def check_multiplicity(amount):
    if amount % 50:
        print_not_multiplicity()
        return 1
    else:
        return 0

def get_amount_removal(amount):
    amount_removal = amount * PERCENT_REMOVAL
    if amount_removal > MAX_REMOVAL:
        amount_removal = MAX_REMOVAL
    elif amount_removal < MIN_REMOVAL:
        amount_removal = MIN_REMOVAL
    return amount_removal

def check_deposit_ge_bank_account(amount):
    amount_removal = int(get_amount_removal(amount))
    if amount > bank_account:
        all_removal = amount + amount_removal
        add_operation(f'Недостаточно средств. Сумма с комиссией {all_removal} у.е. На карте {bank_account} у.е.')
        return 0
    else:
        return amount_removal

def add_deposit(amount):
    global bank_account
    bank_account += amount
    add_operation(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    return 0

def deposit(amount):
    if check_multiplicity(amount):
        return 1
    else:
        return add_deposit(amount)

def do_withdraw(amount, amount_removal):
    global bank_account
    all_removal = amount + amount_removal
    bank_account -= all_removal
    add_operation(f'Снятие с карты {amount} у.е. Процент за снятие {amount_removal} у.е.. Итого {bank_account} у.е.')
    return 0

def withdraw(amount):
    if check_multiplicity(amount):
        check_deposit_ge_bank_account(amount)
        return 1
    # resp is amount removal or 0
    resp = check_deposit_ge_bank_account(amount)
    if not resp:
        return 1
    do_withdraw(amount, resp)

def withdraw_nalog():
    global bank_account
    nalog_value = RICHNESS_PERCENT * bank_account
    bank_account -= nalog_value
    add_operation(f'Вычтен налог на богатство 0.1% в сумме {nalog_value:.4f} у.е. Итого {bank_account:.4f} у.е.')
    return 0

def check_nalog():
    if bank_account > RICHNESS_SUM:
        withdraw_nalog()
        return 1
    else:
        return 0

def exit():
    if check_nalog():
        add_operation(f'Возьмите карту на которой {bank_account:.4f} у.е.')
    else:
        add_operation(f'Возьмите карту на которой {bank_account} у.е.')


deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)