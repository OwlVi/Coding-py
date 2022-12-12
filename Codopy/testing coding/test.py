import numpy as np
income = ["20K", "3M", "12K", "0.04M", "0.023K", "-", "16K", "740K", "15K", "40K",
         "-", "17K", "-", "120K", "56K", "-", "42K", "2M", "0.14M", "60K"]
income = np.char.replace(income,'K','*1000')
income = np.char.replace(income,'M','*1000000')
lits_income = []
for i in range(len(income)):
    if income[i] == '-':
        lits_income.append(np.nan)
    else:
        lits_income.append(eval(income[i]))
income_number = np.array(lits_income)
print(lits_income)
print(type(income_number))
print(income_number.dtype)
print(income_number)
