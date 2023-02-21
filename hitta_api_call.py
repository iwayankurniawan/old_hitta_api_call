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
choose = []
j=0

nama = []
street = ""
number = ""
noRoom = ""
city = ""
zipCode = ""

with open('datadigabung.csv','r') as kbri:

    kbri_reader = csv.reader(kbri)
    next(kbri_reader)

    for linekbri in kbri_reader:
        
        # Get url from first argument
	# linekbri[6] value should look like this STEVEN+EDWARD+GERRARD
        url = "/publicsearch/v1/combined?what=" + linekbri[6]

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
        x = -1
        if json_response['result']['persons']['total'] == 0:
            print ""
            #print " "
        elif json_response['result']['persons']['total'] > 1:
            #print "12" + json_response['result']['persons']['person'][0]['displayName'] + " /" +linekbri[6]+ " "+ str(json_response['result']['persons']['total'])
            print ""
        elif json_response['result']['persons']['total'] == 1:
            for element1 in json_response['result']['persons']['person'][0]:
                choose.append(element1)
            y = -1
            m = False 
            for k in choose:
                y=y+1
                if choose[y]=="address":
                    m = True
                    for element in json_response['result']['persons']['person'][0]['address'][0]:
                        alamat.append(element)
                    for i in alamat:
                        x=x+1
                        if alamat[x]=="street":
                            street = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
                        elif alamat[x]=="number":
                            number = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
                        elif alamat[x]=="apartmentNo":
                            noRoom = "Lgh " + json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
                        #elif alamat[x]=="city":
                            #city = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
                        #elif alamat[x]=="zipcode":
                            #zipCode = json_response['result']['persons']['person'][0]['address'][0][alamat[x]]
                    #printthis = street + " " +number + " "+noRoom +", " +str(zipCode) + " " + city
                    printthis = street + " " +number + " "+noRoom 
                    print printthis
            if not m :
                print " "
                   
                    
                    
                    
        del choose[:]
        del alamat[:]
        
        street = ""
        number = ""
        noRoom = ""
        city = ""
        zipCode = ""
        printthis = ""
        #print json.dumps(json_response, indent=4, separators=(',', ': '))
