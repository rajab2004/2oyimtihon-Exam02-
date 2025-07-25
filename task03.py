def calculate_tax(salary):
    if salary <= 3000000:
        return 0
    elif salary <= 5000000:
        return (salary - 3000000) * 0.1
    elif salary <= 10000000:
        return (salary - 5000000) * 0.15 + 200000
    else:
        return (salary - 10000000) * 0.2 + 950000
def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax