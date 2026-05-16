import json

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
 #json to dictionary
person=json.loads(person_json)
print(person)
print(person['name'])
print(type(person))


#dictionary to JSON

person_dictionary= {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

dic_json=json.dumps(person_dictionary,indent=4)
print(dic_json)
print(type(dic_json))


#saving as json file

with open('./example.json','w',encoding='utf-8') as f:
    json.dump(person_dictionary,f,ensure_ascii=False,indent=4)  #we use encoding and indentation. Indentation makes the json file easy to read.
