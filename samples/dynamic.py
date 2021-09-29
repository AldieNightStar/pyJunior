from pyJunior import *

cname = input("Enter class name: ")

fields = []
while True:
    s = input("Enter field type name [empty when done] Example \"int age\": ")
    if len(s) < 1:
        break
    if not " " in s:
        print("Wrong. Need 2 args. 1 Is given")
        continue
    fields.append(s.split(' ', maxsplit=1))

params = []
for i in fields:
    params.append(jparam(i[0], i[1]))
print(
    jclass(PUBLIC, cname, None, None, *params)
)