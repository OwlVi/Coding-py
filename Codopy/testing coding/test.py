
student=["somchai","somying"]
subject=["datacom","os","comarch"]
#สร้าง dict เก็บคะแนนวิชานิสิต
score_subj={}
#วน loop นักเรียน
for stud in student:
    print (stud)
    score_stud = {}
    for subj in subject: # วนลูปรับคะแนนแต่ละวิชา
        score_stud[subj] = int(input(f'{subj} = '))
    score_subj[stud] = score_stud
    print("-"*5)
print(score_subj)
#เลือกรายชื่อนิสิต
sel_stud = input('Select Nisit : ')
dict_stud = score_subj[sel_stud]
print(dict_stud)
