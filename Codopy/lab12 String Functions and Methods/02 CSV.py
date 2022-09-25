# CSV

text = input()
text = text.split(",")
lst = ''
count = 0
for i in text:
    count += 1 
    i = i.strip()
    i = i.replace(f"{i}",f'''"{i}"''')
    lst += i
    if count < len(text):
        lst += ','
print(lst)