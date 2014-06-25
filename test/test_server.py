#
#
#
import unittest

import ldap

import dhcpmanager

class TestDhcpServer(unittest.TestCase):

    def setUp(self):
        self.hostname = "192.168.1.12"
        self.basedn = "dc=lamourine,dc=homeunix,dc=org"
        self.username = "admin"
        self.password = "oracle"
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
