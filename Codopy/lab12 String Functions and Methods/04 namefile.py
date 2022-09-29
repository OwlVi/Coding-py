# correct the name

text = input()
txtl = ''
txtr = ''
x = True

txtdot = text.rsplit('.',1)
for i in txtdot[0]:
        if i.isalnum() or i in '$':
            txtl += i
        else:
            txtl += '_'
for i in txtdot[-1]:
        if i.isalnum() or i in '$':
            txtr += i
        else:
            txtr += '_'
if '.' in text:
    print(txtl[:15]+f'.{txtr[:3]}')
else:
    print(txtl[:15])