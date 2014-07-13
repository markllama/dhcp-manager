#
# A DHCP Service configuration record
#
from ldapobject import *

class Service(LdapObject):

    filter = '(objectClass=dhcpService)'
    classes = ['top', 'dhcpService']
    attrmap = {
        'cn': 'cn',
        'dhcpPrimaryDN': 'server_dn',
        'dhcpStatements': 'statements',
        'dhcpOption': 'options'
    }

    def __init__(self, dn=None, cn=None, server_dn=None):
        
        super(Service, self).__init__()
        self.dn = dn
        self.cn = cn
        self.server_dn = server_dn

        self.statements = []
        self.comments = []
        self.options = []

        self.server_name = None
        self.server_identifier = None
        self.authoritative = False
        self.dns_update_style = "none"
        self.max_lease_time = 0
        self.default_lease_time = 0
        self.allow_booting = False
        self.allow_boot = False

        self.domain_name = None
        self.domain_name_servers = []


    @classmethod
    def fromldap(cls, ldaphash):
        c = cls()

