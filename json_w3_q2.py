#Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
import json
x={
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(x)
# convert into JSON:
y=json.dumps(x)
# the result is a JSON string:
print(y)
print(type(y))
print(type(x))

