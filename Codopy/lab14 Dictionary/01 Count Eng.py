#Count English Characters
def count_char(word):
    dic = {}
    word = word.lower()
    for i in word:
        if i not in dic and i.isalpha():
            dic[i] = 0
    for i in word:
        if i in dic:
            dic[i] += 1
    return dic

print(count_char('123456'))