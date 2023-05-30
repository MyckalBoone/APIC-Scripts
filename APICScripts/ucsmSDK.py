#! /usr/bin/env python

from ucsmsdk.ucshandle import UcsHandle

IP = input('Enter the IP Address: ')
USERNAME = input('Enter your username: ')
PASSWORD = getpass()

Handle = UcsHandle('"'+ IP + '"','"'+ USERNAME +'"','"' + PASSWORD + '"')

# Login into Cisco UCS Manager
Handle.login()

#Retrieve all the compute blades
Blades = Handle.query_classid("ComputeBlade")

print ('{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}'.format( "DN", "SERIAL", "ADMIN STATE", "MODEL", "TOTAL MEMORY"))
print ('-'*70)


# Extract DN, SN, admin state model, and total memory for each blade
for BLADE IN BLADES:
    print ('{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}'.format(BLADE.dn, BLADE.serial, BLADE.admin_state, BLADE.model, BLADE.total_memory))

HANDLE.logout()
