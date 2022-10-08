# def namelist

def namelist(names):
    x = ''
    if len(names) > 1 and '' not in names :
        x = f"{', '.join(names[:len(names)-1])}" + f' & {names[-1]}'
    elif len(names) == 1 :
        x = f'{names[-1]}'
    return x
print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )