#!/usr/bin/env python3

import logging
if False:
    logging.basicConfig(filename='auto_tag.log', filemode='w', level=logging.ERROR)

import json
import sys
from pathlib import Path


OLD = json.loads(sys.stdin.readline())

try:
    OLD = json.loads(sys.stdin.readline())
except Exception:
    pass


new = OLD.copy()

with open(str(Path.home()) + '/.task/hooks/tags.config', 'r') as tag_config_file:
    TAG_CONFIG = json.load(tag_config_file)


if 'tags' not in list(OLD):
    print(json.dumps(new))
    exit()

num_tags_old = 0
while True:
    logging.debug(f"num_tags_old: {num_tags_old}")
    if num_tags_old == len(new['tags']):
        break
    num_tags_old = len(new['tags'])
    for tag1 in list(TAG_CONFIG):
        if tag1 in list(new['tags']):
            if type(TAG_CONFIG[tag1]) is list:
                for tag_to_add in TAG_CONFIG[tag1]:
                    if tag_to_add not in new['tags']:
                        new['tags'].append(tag_to_add)
            else:
                if TAG_CONFIG[tag1] not in new['tags']:
                    new['tags'].append(TAG_CONFIG[tag1])



print(json.dumps(new))
