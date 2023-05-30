#! /usr/bin/env python

import sys

import acittoolkit.acitoolkit as aci

APIC_URL = input('Enter the APIC_URL: ')
USERNAME = input('Enter your username: ')
PASSWORD = getpass()

# Login into APIC
SESSION = aci.Session(APIC_URL, USERNAME, PASSWORD)
RESP = SESSION.login()
if not RESP.ok:
    print ('Could not login to APIC')
    sys.exit()

ENDPOINTS = aci.Endpoint.get(SESSION)
print ('{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}'.format( "MAC ADDRESS", "IP ADDRESS", "ENCAP", "TENANT", "APP PROFILE", "EPG"))
print ('-'*80)


# Extract MAC ADDRESS, IP ADDRESS, ENCAP, TENANT, APP PROFILE, and EPG
for EP in ENDPOINTS:
    epg = EP.get_parent()
    app_profile = epg.getparent()
    tenant = app_profile.getparent()

    print ('{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}'.format(ENDPOINTS.mac, ENDPOINTS.ip, ENDPOINTS.encap, tenant.name, app_profile.name, epg.name))
