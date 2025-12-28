import json

# data = {"name": "Krish", "age": 22,"active":True,"active1":False,"active2":None}
# json_data = json.dumps(data)  
# print(json_data)
# print(type(json_data))

# data ='{"name": "Krish","active":true, "age": 22}'
# json_data = json.loads(data)  
# print(json_data)



data ='{"name": "Krish", "age": 22, "active": true, "active1": false, "active2": null}'
json_data = json.loads(data)  
print(json_data)
