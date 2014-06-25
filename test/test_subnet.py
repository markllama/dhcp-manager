#!/usr/bin/python
#

import unittest

import ldap

import dhcpmanager

class TestSubnet(unittest.TestCase):

    def setUp(self):
        self.hostname = "192.168.1.12"
        self.basedn = "dc=lamourine,dc=homeunix,dc=org"
        self.username = "admin"
        self.password = "oracle"
        self.connection = ldap.initialize("ldap://%s" % self.hostname)
        self.binddn = "cn=%s,%s" % (self.username, self.basedn)
        r = self.connection.simple_bind_s(self.binddn, self.password)
        
    def tearDown(self):
        pass

    def testSubnetConstructor(self):
        baseaddr = "10.19.136.0"
        netmask = "255.255.248.0"
        gateway = "10.19.143.254"

        subnet = dhcpmanager.Subnet(baseaddr, netmask)

        self.assertEqual(baseaddr, str(subnet.baseaddr))
        self.assertEqual(21, subnet.netmask)

    def testSubnetRetrieve(self):

        baseaddr = "192.168.1.0"
        netmask = 24

        n = dhcpmanager.Subnet.retrieve(self.connection, self.basedn, baseaddr)
        self.assertEqual(baseaddr, n.baseaddr)
        self.assertEqual(netmask, n.netmask)
        self.assertEqual(1, len(n.routers))

    def testSubnetCommit(self):

        baseaddr = "172.16.1.0"
        netmask = "21"
        gateway = "172.16.8.254"

        n = dhcpmanager.Subnet(baseaddr, netmask, gateway)
        #n.commit(self.connection, server)

if __name__ == "__main__":

    unittest.main()
