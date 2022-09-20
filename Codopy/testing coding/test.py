word = input()
original = ''
n = 0
count = 0

for i in word :
  if count != n :
    count += 1
    continue
  if count + 2 < len(word) :
    if word[n] == word[n+2] and word[n] in 'aeiou' and word[n+1] == 'p' :
      original += i
      n += 3
    else :
      original += i
      n += 1
  else :
    original += i
    n += 1
  count += 1
    
print(original)