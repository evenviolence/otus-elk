#!/usr/bin/python3.6

import json

l = []
for i in range(1,4):
   d = { "{#METRIC}" : "metric"+str(i)}
   l.append(d)
data = { "data" : l}
app = json.dumps(data)
print(app)
