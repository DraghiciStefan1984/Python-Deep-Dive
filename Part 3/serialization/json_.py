import json


d1={'a': 100, 'b': 200}
d1_json=json.dumps(d1)
print(d1_json)

d2=json.loads(d1_json)
print(d1 is d2)