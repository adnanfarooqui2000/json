import json
python_data={
    'name':'Adnan',
    'quli':'b.com comp',
    'city_Bhopal':True,
    'belong':False,
    'activity':None,
}
print (json.dumps(python_data))
print(type(json.dumps(python_data)))
data='{"Name":"Adnan","Quli":"B.com (comp)","City_bhopal":true,"belongs":false,"Activity":"null"}'
print(json.loads(data))