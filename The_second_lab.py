#! /usr/bin/env python3

import os
import requests

the_dir = "/data/feedback/"

txt_files =os.listdir (the_dir)
list_keys = ["title", "name", "date", "feedback"]

for txt in txt_files:
    count = 0
    feedback = {}
    with open (the_dir + txt) as file:
        for line in file:
            value = line.strip()
            feedback[list_keys[count]] = value
            count += 1
    print (feedback)
    respones = requests.post("http://<<your external IP>>/feedback/", json=feedback)

print (respones.request.body)
print (respones.status_code)
