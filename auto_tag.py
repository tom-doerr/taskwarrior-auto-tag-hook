#!/usr/bin/env python3

import json
import sys
from pathlib import Path

OLD = json.loads(sys.stdin.readline())

try:
    OLD = json.loads(sys.stdin.readline())
except Exception:
    pass


#print('Input: ' + str(OLD))
new = OLD.copy()

with open(str(Path.home()) + '/.task/hooks/tags.config', 'r') as tag_config_file:
    TAG_CONFIG = json.load(tag_config_file)


if 'tags' not in list(OLD):
    print(json.dumps(new))
    exit()


for tag1 in list(TAG_CONFIG):
    if tag1 in list(OLD['tags']):
        #print('Found ' + str(tag1) + ' in tags')
        if type(TAG_CONFIG[tag1]) is list:
            for tag_to_add in TAG_CONFIG[tag1]:
                new['tags'].append(tag_to_add)
        else:
            new['tags'].append(TAG_CONFIG[tag1])



#print('Output: ' + str(new))

print(json.dumps(new))
