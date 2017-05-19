import json

dept_list=[]
a=raw_input()
while(a!='exit'):
    dept_list.append(a)
    a=raw_input()

with open("dept_list.json",'wb') as output:
    json.dump(dept_list,output)
