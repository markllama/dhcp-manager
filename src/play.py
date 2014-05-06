#!/usr/bin/python
#
# Connect to an LDAP server and make queries for DHCP servers
#
import ldap
import ldaphelper

hostname = "pi1.lamourine.homeunix.org"
binddn = "cn=admin,dc=lamourine,dc=homeunix,dc=org"
bindpw = "oracle"
basedn = "dc=lamourine,dc=homeunix,dc=org"
filter = "(objectClass=dhcpHost)"
attrs = ['cn']

if __name__ == "__main__":
    c = ldap.initialize("ldap://%s" % hostname)
    try:
        # 
        result = c.simple_bind_s(binddn, bindpw)
        print result
    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            print e.message['desc']
        else: 
            print e
            sys.exit()

    r = c.search_s(basedn, ldap.SCOPE_SUBTREE, filter, attrs)
    results = ldaphelper.get_search_results(r)
    print "\n".join([h.get_dn() for h in results])
