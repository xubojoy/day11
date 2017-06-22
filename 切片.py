#Author:xubojoy
word = 'Python'
print(word[:2])

list = [(x, y) for x in [1,2,3] for y in [3,4,1] if x != y]
print(list)

words = ['cat', 'window', 'defenestrate']

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print(words)

for i in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(i, i*i, i*i*i))


# f = open('workfile', 'w')
with open('workfile', 'r') as f:
    read_data = f.read()
    print('-------------',read_data)
    f.close()

import json
j = json.dumps([1, 'simple', 'list'])

print(json.loads(j))

import requests
from requests.auth import HTTPBasicAuth

# r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
print(r.json())