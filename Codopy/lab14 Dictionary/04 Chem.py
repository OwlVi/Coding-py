# Chemical Formular ONE
def chem(text):
    txt = ''
    data = []
    for i in range(len(text)):
        txt += text[i]
        if (i == len(text)-1):
            data.append(txt)
            txt = ''
        elif text[i].islower() and (text[i+1].isupper() or text[i+1].isdigit()):
            data.append(txt)
            txt = ''
        elif(text[i].isupper() and text[i+1].isdigit() ):
            data.append(txt)
            txt = ''
        elif (text[i].isdigit() and not text[i+1].isdigit()):
            data.append(txt)
            txt = ''
        elif (text[i].isupper() and not text[i+1].islower()):
            data.append(txt)
            txt = ''
    return data
dic = {}
data= []
txt = input()
n   = input()
for i in range(len(chem(txt))):
    if chem(txt)[i] not in dic:
        if chem(txt)[i].isdigit():
            dic[chem(txt)[i-1]] += int(chem(txt)[i])-1
        else:
            dic[chem(txt)[i]] = chem(txt).count(chem(txt)[i])
if n in dic:
    print(dic[n])
else:
    print('0')