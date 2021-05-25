def total_expense(expenses):
    e = 0
    for i in expenses:
        e = e + i.expense
    return e

def total_remaining(project,expenses):
    e = project.budget_allocated
    for i in expenses:
        e = e - i.expense
    return e