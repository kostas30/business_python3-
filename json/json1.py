import json
student_json = '{"name" : "Γιάννης", "age":20, "courses":["Φυσική", "Μαθηματικά"]}'
print(student_json)
student = json.loads(student_json)
# print(f"courses ειναι :",student['courses'])

newjson = json.dumps(student)
print(newjson)