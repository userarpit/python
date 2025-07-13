import json
import jmespath

x = {
    "people": [
        {
            "first":"Arpit",
            "last":"Khandelwal",
            "age":30
        },
        {
           "first":"Abcd",
           "last":"Khandelwal",
           "age":35
        }
        ]}

expr1 = {"foo": {"bar": "baz"}}

y = json.dumps(x,indent=4)
print(y)

# print(json.loads(y))

with open("conda.txt","w") as file:
    json.dump(x,file)

with open("conda.txt",'r+') as file:
    print(json.load(file))

print(jmespath.search('foo',expr1))

list1 = [1,2,3,4,"arpit"]
print(json.dumps(list1,indent=4,sort_keys=True))

print(jmespath.search("people[?first=='Abcd']",x))
print(jmespath.search("people[*].first | [1]",x))
print(jmespath.search("people[].{first:first,last:last}",x))


y = {
  "people": [
    {
      "age": 20,
      "other": "foo",
      "name": "Bob"
    },
    {
      "age": 25,
      "other": "bar",
      "name": "Fred"
    },
    {
      "age": 30,
      "other": "baz",
      "name": "George"
    }
  ]
}

print(jmespath.search("people[?age>=`20`].[name, age] | [2]",y))
