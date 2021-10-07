import os
import discord
import feedparser
import json

from dotenv import load_dotenv
load_dotenv()

print('run pyBot')
with open('data.json', 'w') as f:
    json.dump([], f, indent=4)

output = json.load(open('data.json'))

feed = feedparser.parse('http://127.0.0.1:3000/rss')
print('feed', feed)

obj = {}
item = 0
for x in feed['entries']:
    print('xxx', x)
    obj = {
        'id': item,
        'title': x['title']
    }
    output.insert(len(output) -1, obj)
    item += 1

with open('data.json', 'w') as f:
    json.dump(output, f, indent=4)

print('feed2', output)
