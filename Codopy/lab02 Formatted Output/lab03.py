#type
#input
inc = float(input())
ex  = float(input())
# output
print("1234567890" * 3)
print("{:<13s}{:+8.2f}{:>6s}".format("Total Income",inc,"bahts"))
print("{:<13s}{:8.2f}{:>6s}".format("Expense",ex,"bahts"))
print("{:<13s}{:08.2f}{:>6s}".format("Profit",inc+ex,"bahts"))