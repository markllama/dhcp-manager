#
#
#
import unittest

import ldap

import dhcpmanager

from auth import ldap_server

class TestDhcpServices(unittest.TestCase):

    def setUp(self):
        self.hostname = ldap_server['hostname']
        self.basedn = ldap_server['basedn']
        self.username = ldap_server['username']
        self.password = ldap_server['password']
        self.connection = ldap.initialize("ldap://%s" % self.hostname)
        self.binddn = "cn=%s,%s" % (self.username, self.basedn)
        r = self.connection.simple_bind_s(self.binddn, self.password)

    def testConstructor(self):
        s = dhcpmanager.Service()

    def testListServices(self):
        services = dhcpmanager.Service.list(self.connection, self.basedn)
        print services

    def testRetrieveService(self):
        server_cn = 'pi1'
        s = dhcpmanager.Service(cn=server_cn)
        s.retrieve(self.connection, self.basedn)

        self.assertEqual(len(s.classes), 2)
        self.assertEqual(s.cn, 'DHCP Config')
        self.assertEqual(len(s.statements), 8)
        self.assertEqual(len(s.options), 2)
        
if __name__ == "__main__":
    unittest.main()
