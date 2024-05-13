''' build a mortgage calculator that takes
in loan amount, APR, and loan duration and returns the
monthly payment assuming that interest is compounded monthly.'''

import json
with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def welcome():
    prompt(MESSAGES["welcome"])
    print()

def try_again_message():
    print("-------PLEASE TRY AGAIN!-------")

def get_loan_amount():
    prompt(MESSAGES["loan_amount"])
    loan_amount_input = input()
    return loan_amount_input

def invalid_loan_amount(input_value):
    try:
        float(input_value)
        if float(input_value) <= 0:
            return True
    except ValueError:
        return True
    return False

def get_apr():
    prompt(MESSAGES["APR"])
    annual_percentage_rate_input = input()
    return annual_percentage_rate_input

def invalid_apr(input_apr):
    try:
        float(input_apr)
        if float(input_apr) < 0:
            return True
    except ValueError:
        return True
    return False

def get_loan_year_duration():
    prompt(MESSAGES["years"])
    year_duration = input()
    while invalid_loan_duration(year_duration):
        prompt(MESSAGES["invalid_year"])
        year_duration = input()
    year_month_conversion = int(year_duration) * 12
    return year_month_conversion

def get_loan_month_duration():
    prompt(MESSAGES["months"])
    month_duration = input()
    while invalid_loan_duration(month_duration):
        prompt(MESSAGES["invalid_months"])
        try_again_message()
        month_duration = input()
    month_duration = int(month_duration)
    return month_duration

def invalid_loan_duration(loan_duration):
    try:
        int(loan_duration)
        if int(loan_duration) < 0:
            return True
    except ValueError:
        return True
    return False

def zero_or_less_duration(year_month_conversion, month_duration):
    duration = year_month_conversion + month_duration
    if duration <= 0:
        return True
    return False

def calc_again():
    prompt(MESSAGES["another_calculation"])
    another_calc = input()
    if another_calc.lower() == 'y':
        return loan_calculator()

    return prompt(MESSAGES["bye"])

def loan_calculator(): # LOAN CALC PROGRAM
    welcome()

    # LOAN AMOUNT INPUT:
    loan_amount_input = get_loan_amount()
    while invalid_loan_amount(loan_amount_input):
        prompt(MESSAGES["invalid_loan_amount"])
        try_again_message()
        loan_amount_input = input()
    loan_amount = float(loan_amount_input)

    # MONTHLY APR:
    annual_percentage_rate_input = get_apr()
    while invalid_apr(annual_percentage_rate_input):
        prompt(MESSAGES["invalid_apr"])
        try_again_message()
        annual_percentage_rate_input = get_apr()
    annual_percentage_rate = float(annual_percentage_rate_input)

    if annual_percentage_rate != 0:
        # CONVERT APR TO DECIMAL FORMAT
        annual_percentage_rate = float(annual_percentage_rate_input) * .01
        # APR -> MONTHLY INTEREST RATE
        monthly_interest_rate = annual_percentage_rate / 12
    else:
        annual_percentage_rate = 'No APR'

    # LOAN DURATION:
    prompt(MESSAGES["loan_duration"])
    year_month_conversion = get_loan_year_duration()
    month_duration = get_loan_month_duration()

    # CHECK TOTAL LOAN DURATION IS GREATER THAN 0:
    while zero_or_less_duration(year_month_conversion, month_duration):
        prompt(MESSAGES["invalid_loan_duration"])
        try_again_message()
        year_month_conversion = get_loan_year_duration()
        month_duration = get_loan_month_duration()

    loan_duration_months = year_month_conversion + month_duration

    # MONTHLY PAYMENT with VS without APR:
    if annual_percentage_rate != 'No APR':
        monthly_payment_apr = loan_amount * (monthly_interest_rate /
        (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
        prompt(f'Your monthly payment is: ${monthly_payment_apr:.2f}')
    else:
        monthly_payment =  loan_amount / loan_duration_months
        prompt(f'Your monthly payment is: ${monthly_payment:.2f}')

    # ASK USER IF THEY WANT TO CALC AGAIN:
    print()
    calc_again()

loan_calculator()