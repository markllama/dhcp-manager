#
#
#
import unittest

import ldap

import dhcpmanager

from auth import ldap_server

class TestDhcpServer(unittest.TestCase):

    def setUp(self):
        self.hostname = ldap_server['hostname']
        self.basedn = ldap_server['basedn']
        self.username = ldap_server['username']
        self.password = ldap_server['password']
        self.connection = ldap.initialize("ldap://%s" % self.hostname)
        self.binddn = "cn=%s,%s" % (self.username, self.basedn)
        r = self.connection.simple_bind_s(self.binddn, self.password)

    def testConstructor(self):
        s = dhcpmanager.Server()

    def testListServers(self):
        servers = dhcpmanager.Server.list(self.connection, self.basedn)
        print servers

if __name__ == "__main__":
    unittest.main()
