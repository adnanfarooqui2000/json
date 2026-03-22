import json
python_data={
    'name':'Adnan',
    'quli':'B.com (computer Application)',
    'city_Bhopal':True,
    'belong':False,
    'activity':None,
}
print (json.dumps(python_data))
print(type(json.dumps(python_data)))
data='{"Name":"Adnan","Quli":"B.com (computer Application)","City_bhopal":true,"belongs":false,"Activity":"null"}'
print(json.loads(data))