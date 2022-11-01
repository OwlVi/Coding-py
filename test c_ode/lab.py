def extract_string(text):
    txt = ''
    data = []
    for i in range(len(text)):
        txt += text[i]
        if i == (len(text)-1) or (not text[i].isdigit() and text[i+1].isdigit()) or ( text[i].isdigit() and not text[i+1].isdigit()):
                if txt.isdigit():
                    data.append(int(txt))
                else:
                    data.append(txt)
                txt = ''
    return data
print( extract_string("G2X3t4") )
print( extract_string("AB12XY23") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )