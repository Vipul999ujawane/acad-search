import urllib2
import pprint
from bs4 import BeautifulSoup
import json

dept_list=open("dept_list.json").read()
data=json.loads(dept_list)
sub_list=[]
pk=1;
for i in data:
    url=urllib2.urlopen("https://erp.iitkgp.ernet.in/ERPWebServices/curricula/CurriculaSubjectsList.jsp?stuType=UG&splCode="+i)
    content=url.read()
    soup=BeautifulSoup(content,"html.parser")
    table=soup.find_all('table')
    for line in table:
        for row in line.find_all('tr'):
            tab = row.find_all('td',style="background-color: white")
            if tab is not None and len(tab) > 0:
                if len(tab[2].text)>0:
                    if tab[2].text[0]==" ":
                        sub_code=tab[2].text[1:]
                    else:
                        sub_code=tab[2].text
                    fields={"department_code":sub_code[:2],"subject_code":sub_code,
                            "subject_name":tab[3].text}
                    test={}
                    test["pk"]=pk
                    test["model"]="acads.subject"
                    test["fields"]=fields
                    found=0
                    for i in range(len(sub_list)):
                        if(sub_list[i]["fields"]["subject_code"]==test["fields"]["subject_code"]):
                            found+=1
                    print found
                    if(found==0):
                        sub_list.append(test)
                        pk+=1
print sub_list
with open("sub_list.json","wb") as data:
    json.dump(sub_list,data)
