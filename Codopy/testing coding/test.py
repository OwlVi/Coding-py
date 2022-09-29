camel = input()
i = 0
new = ''
while i < len(camel) :
  if i > 0 and camel[i-1] in '-_=.$' :
    new += camel[i].upper()
  elif camel[i] not in '-_=.$' :
    new += camel[i].lower()
  i += 1

print(new)