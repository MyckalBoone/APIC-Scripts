#! /usr/bin/env python

# Generic APIC REST API below
# https://APIC_HOST:port/api/{mo|class}/{dn|classname}.{xml|json}?[options]


import requests

USERNAME = input('Enter APIC username: ')
PASSWORD = getpass()
APIC_HOST = input('Enter the APIC Host' )
URL = "https://" + APIC_HOST + "/api/aaalogin.json"

payload = {'aaaUser':{'attributes':{'name':USERNAME, 'pwd': PASSWORD}}}'


headers = {'content-type', "application/json"}{'aaaUser':{'attributes':{'name':USERNAME, 'pwd': PASSWORD}}}'

response = requests.request("POST", URL, headers=headers, data=payload)

APIC_COOKIE = json.loads(response.text)

print (APIC_COOKIE)
