# correct the name

text = input()
if '.' in text:
    text = text.rsplit('.',1)

    for i in range(len(text)):
        text[i] = text[i].replace(" ","_")
        text[i] = text[i].replace(".","_")
        text[i] = text[i].replace("/","_")
        text[i] = text[i].replace(f'{chr(92)}',"_")
        text[i] = text[i].replace("*","_")
        text[i] = text[i].replace(":","_")
        text[i] = text[i].replace('"',"_")
        text[i] = text[i].replace("|","_")
        text[i] = text[i].replace("<","_")
        text[i] = text[i].replace(">","_")
    
    if len(text) == 2:
        if len(text[0]) > 15:
            text[0] = text[0][:15]
        if len(text[1]) > 3 :
            text[1] = text[1][:3]
        print(f"{text[0]}"+'.'+f"{text[1]}")
    else:
        print(text[0][:15])
else:
    text = text.replace(' ','_')
    print(text[:15])