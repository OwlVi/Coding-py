# aeiou.upper
text = input()
newtext = ''
for i in range(len(text)):
    if text[i] in 'aeiouAEIOU':
        newtext += text[i].upper()
    else:
        newtext += text[i].lower()
print(newtext)