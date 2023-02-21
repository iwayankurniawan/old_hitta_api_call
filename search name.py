#!/usr/bin/env python
import sys
import time
import random
import string
import hashlib
import httplib
import json
import csv

time= str(int(time.time()))
random = "".join(random.choice(string.digits) for _ in range(16))

alamat = []
x = -1
j=0

nama = []
choose = []
street = ""
number = ""
noRoom = ""
city = ""
zipCode = ""

# Get url from first argument
url = "/publicsearch/v1/combined?what=asnita"

# Authentication parameters
caller_id = 'wawan'
#time= str(int(time.time()))
key =  '<key from hitta>'
#random = "".join(random.choice(string.digits) for _ in range(16))

# Create the hashed string
string_to_hash = caller_id + time + key + random
hashed_string = hashlib.sha1(string_to_hash).hexdigest()

# The http headers
headers = {
    "X-Hitta-CallerId": caller_id,
    "X-Hitta-Time": time,
    "X-Hitta-Hash": hashed_string,
    "X-Hitta-Random": random
}

# Make the call
conn = httplib.HTTPSConnection("api.hitta.se")
conn.request("GET", url,"",headers)
resp = conn.getresponse()

# Print response
#print resp.status, resp.reason
#print
json_response = json.loads(resp.read())

X=-1
for element in json_response['result']['persons']['person'][0]['address'][0]:
        alamat.append(element)
for i in alamat:
    x=x+1
    if alamat[x]=="street":
        street = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
    elif alamat[x]=="number":
        number = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
    elif alamat[x]=="apartmentNo":
        noRoom = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
    elif alamat[x]=="city":
        city = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
    elif alamat[x]=="zipcode":
        zipCode = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]

            
alamat.clear() 
printthis = street + " " +number + " "+noRoom +", " +city + " " + str(zipCode)
print printthis
#print json.dumps(json_response, indent=4, separators=(',', ': ')) 

