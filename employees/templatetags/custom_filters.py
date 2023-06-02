from django import template
register = template.Library()

@register.filter
def total_earnings(transaction_list):
    total = 0
    for transaction in transaction_list:
        total += transaction.price
    return total

@register.filter
def total_sales_earnings(transactions):
    total_sales = 0
    for transaction in transactions:
        if transaction.t_type == 'Bought':
            total_sales += transaction.price
    return total_sales

@register.filter
def total_repair_earnings(transactions):
    total_repair = 0
    for transaction in transactions:
        if transaction.t_type == 'Repair':
            total_repair += transaction.price
    return total_repair

@register.filter
def total_consult_earnings(transactions):
    total_consult = 0
    for transaction in transactions:
        if transaction.t_type == 'Consult':
            total_consult += transaction.price
    return total_consult

# Register the custom filters
register.filter('total_earnings', total_earnings)
register.filter('total_sales_earnings', total_sales_earnings)
register.filter('total_repair_earnings', total_repair_earnings)
register.filter('total_consult_earnings', total_consult_earnings)
