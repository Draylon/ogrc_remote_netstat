'''from easysnmp import Session

# Create an SNMP session to be used for all our requests
session = Session(hostname='192.168.1.3', community='public', version=2)

# You may retrieve an individual OID using an SNMP GET
location = session.get('sysLocation.0')

# You may also specify the OID as a tuple (name, index)
# Note: the index is specified as a string as it can be of other types than
# just a regular integer
contact = session.get(('sysContact', '0'))

# And of course, you may use the numeric OID too
description = session.get('.1.3.6.1.2.1.1.1.0')

# Set a variable using an SNMP SET
session.set('sysLocation.0', 'The SNMP Lab')

# Perform an SNMP walk
system_items = session.walk('system')

# Each returned item can be used normally as its related type (str or int)
# but also has several extended attributes with SNMP-specific information
for item in system_items:
    print('{oid}.{oid_index} {snmp_type} = {value}'.format(
        oid=item.oid,
        oid_index=item.oid_index,
        snmp_type=item.snmp_type,
        value=item.value
    ))
'''

from easysnmp import Session

#session = Session(hostname='192.168.1.1', community='public', version=1)

session = Session(hostname= '192.168.1.3',community='public', version=3,security_username= 'bootstrap',auth_password= 'udescUdesc',privacy_password= 'udescUdesc',security_level= 'authPriv',auth_protocol= 'MD5',privacy_protocol="DES")

#location = session.walk('.3.6.1.2.1.4.21.1')
#location = session.walk('system')

#location = session.walk('1.3.6.1.2.1.7')
#location = session.walk('1.3.6.1.2.1.4.21.1.3')
#location = session.walk('1.3.6.1.2.1.6') # TCP
#location = session.walk('1.3.6.1.2.1.7') # UDP


location = session.walk('.1.3.6.1.2.1.6.13.1.1') # TCP
#location = session.walk('.1.3.6.1.2.1.7.7')
#location = session.walk('.1.3.6.1.2.1.7.7')


#location = session.get('sysLocation.0')
#location = session.get('.iso.org.dod.internet.mgmt.mib-2.system.sysLocation.0')
#location = session.get('.1.3.6.1.2.1.1.1')
#location = session.get('iso.sysUpTime.0')
#location = session.get('iso.3.6.1.2.1.1.6.0')
#location = session.get('iso.1.3.6.1.2.1.1.1.0')
#location = session.get('.1.3.6.1.2.1.1.3')
#location = snmp_walk('.1.3.6.1.2.1.1', hostname='192.168.1.3', community='public', version=2)

f = open("omegalul.txt", "w")
f.write(str(location))
f.close()
#print(location)
