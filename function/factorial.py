def factorial_table(i):

    count = 2
    res = 1
    fac = '1'
    if i < 0:
        print(f'Invalid input, program terminates.')
    else:
        while count <= i:
            fac = f'{count} x ' + fac
            count += 1
        factorial_str = f"{i}! = {fac}"
    return factorial_str

print(factorial_table(0))