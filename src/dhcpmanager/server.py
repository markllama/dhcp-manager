#
#
#
import ldap

from ldapobject import *

class Server(LdapObject):

   filter = '(objectClass=dhcpServer)'
   classes = ['top', 'dhcpServer']
   attrmap = {
      'objectClass': 'classes',
      'cn': 'cn',
      'dhcpServiceDN': 'service_dn',
      'dhcpLocatorDN': 'locator_dn',
      'dhcpVersion': 'version',
      'dhcpImplementation': 'implementation',
      'dhcpHashBucketAssignment': 'hash_bucket_assignment',
      'dhcpDelayedServiceParameter': 'delayed_service_parameter',
      'dhcpMaxClientLeadTime': 'max_client_lead_time',
      'dhcpFailOverEndpointState': 'failover_endpoint_state',
      'dhcpStatements': 'statements',
      'dhcpComments': 'comments',
      'dhcpOption': 'option' 
   }

   def __init__(self, dn=None, cn=None, service_dn=None):

      super(Server, self).__init__()
      self.dn = dn
      self.cn = cn
      self.service_dn = service_dn

      self.locator_dn = None
      self.version = None
      self.implementation = None
      self.hash_bucket_assignment = None
      self.delayed_service_parameter = None
      self.max_client_lead_time = None
      self.failover_endpoint_state = None

      self.statements = []
      self.commments = []

      self.options = []
      # declarations
      # self.primary # true = primary, false = secondary
      # self.address #
      # self.port #
      # self.peer_address #
      # self.peer_port #
      # self.max_response_delay
      # self.max_unacked_updates
      # self.max_client_lead_time # mclt
      # self.split
      # self.hba
      # self.load_balance_max_seconds
      # 

