#
#
#
import ldap

class LdapObject(object):

   filter = None
   object_classes = []
   attrmap = {}
   required = ['cn']

   def __init__(self, dn=None):
      self.dn = dn
      for k in self.__class__.attrmap.keys():
         self.__dict__[self.__class__.attrmap[k]] = None

   @classmethod
   def create(cls, connection):
      pass

   @classmethod
   def list(cls, connection, basedn):
      attrs = []
      r = connection.search_s(basedn, ldap.SCOPE_SUBTREE, cls.filter)
      return r

   def retrieve(self, connection, basedn):
      filter = "(& %s (cn=%s))" % (self.__class__.filter, self.cn)
      r = connection.search_s(basedn, ldap.SCOPE_SUBTREE, self.__class__.filter)
      if len(r) != 1:
         raise "wrong number of matches: expected 1, actual %d" % len(r)
      (dn, attrs) = r[0]
      
      self.dn = dn
      for k in attrs:
         if k in self.__class__.attrmap.keys():
            if len(attrs[k]) == 1:
               self.__dict__[self.__class__.attrmap[k]] = attrs[k][0]
            else:
               self.__dict__[self.__class__.attrmap[k]] = attrs[k]
         else:
            print "attr %s not in attrmap" % k
