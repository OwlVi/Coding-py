# AROIIII

#input 
txt = input()
ntxt = ''
txt = txt.strip()
txt = txt.title()

for i in ['-','_','=','.','$']:
    if i in txt:
        txt = txt.replace(i,'')
if txt in '':
    ntxt = txt
else:
    if txt[0].islower():
        pass
    else:
        ntxt += txt[0].lower()
        ntxt += txt[1:]
        
#output
print(ntxt)