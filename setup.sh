#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ln -s $DIR"/tags.config" ~/.task/hooks/tags.config
ln -s $DIR"/auto_tag.py" ~/.task/hooks/on-add.auto_tag.py
ln -s $DIR"/auto_tag.py" ~/.task/hooks/on-modify.auto_tag.py

