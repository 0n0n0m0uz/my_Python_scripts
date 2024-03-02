
#prettyprint raw JSON Data

import json
with open('newest.json', 'r') as handle:
    parsed = json.load(handle)
print(json.dumps(parsed, indent=4, sort_keys=True))

# or print to a file
j = json.dumps(parsed, indent=4, sort_keys=True)
f = open('sample.json', 'w')

print(j, file=f)
