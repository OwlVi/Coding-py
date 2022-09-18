# mosssy a e i o u

text = input()
count = 0
while count < len(text):
    for i in text:
        if i in 'aeiou':
            text = text.replace(f"{i}p{i}",f"{i}")
    count += 1
print(text)

