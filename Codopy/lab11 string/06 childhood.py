# mosssy a e i o u
def lst(x):
    lst = []
    for i in x:
        lst += i
    return lst
text = input()
text = lst(text)
newtext = ''
i = 0
while i < len(text):
    if text[i] in 'aeiou' and text[i] == text[i-2]:
        text[i-2:i] = []
    i += 1
for i in text:
    newtext += i
print(newtext)

