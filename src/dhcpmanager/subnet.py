#
#
#
import ipaddr
import ldap

class Subnet(object):
    """Represent a DHCP Subnet entry in an LDAP database"""
    
    def __init__(self, baseaddr, netmask, routers=None):

        self._ipnet = ipaddr.IPv4Network(baseaddr + '/' + netmask)
        self._routers = routers

    @staticmethod
    def retrieve(connection, basedn, baseaddr):
        filters = "(&(objectClass=dhcpSubnet) (cn=%s))" % baseaddr
        r = connection.search_s(basedn, ldap.SCOPE_SUBTREE, filters)

        if r == None or r == []: return None
        if len(r) > 1:
            raise "Ambiguous network match"

        (dn, attrs) = r[0]

        baseaddr = attrs['cn'][0]
        netmask = attrs['dhcpNetMask'][0]
        options = attrs['dhcpOption']
        routers = [o.split()[1:] for o in options if  o.startswith('routers ')]
        return Subnet(baseaddr, netmask, routers)

    @property
    def baseaddr(self):
        return str(self._ipnet.network)

    @property
    def netmask(self):
        return self._ipnet.prefixlen


    @property
    def routers(self):
        return self._routers

    @routers.setter
    def routers(self, value):
        self._routers = value


    def commit(self, connnection, server):
        pass
