import json

history = [
    {
        "name": "Alf",
        "age": 29
    }
]

obj = {
    "name": "Brdeuno",
    "age": 21
}

def integrateToJson(data):
    print('Construction')
    history = json.load(open('./data.json'))
    history.insert(1, data)
    with open('data.json', 'w') as f:
        json.dump(history, f, indent=4)

integrateToJson(obj)
