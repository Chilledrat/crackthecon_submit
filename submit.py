#!/usr/bin/env python2

import re
import sys
import json
import requests
import codecs

decode_hex = codecs.getdecoder("hex_codec")

if len(sys.argv) != 2:
    sys.exit("Usage: %s cracked_hashes.txt" % sys.argv[0])

baseurl = 'https://crackthecon.com/api/submit.php'

tokenpath, token = 'token', ''

if len(tokenpath) > 0:
    with open(tokenpath, 'r') as token_file:
        token = token_file.read().rstrip()
else:
    token = 'Add your token here'

if not re.match('^[0-9A-Za-z]{64}$', token):
    sys.exit('Check your token.')

count = 0
founds = []
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        line = line.rstrip('\r\n')
        pos = line.find('$HEX[')
        if pos > -1:
            prefix = line[:pos]
            pw_dec = decode_hex(line[pos + 5:-1])[0]
            print(pw_dec)
            line = prefix + pw_dec.decode()
        founds.append(line)

data = {u"key": token, u"found": founds}
print(json.dumps(data, indent=4))
# response = requests.post(baseurl, json.dumps(data))
#print(response.content)
