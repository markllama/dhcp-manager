#
#
#
import ldap
import types

class LdapObject(object):

   filter = None
   object_classes = []
   attrmap = {}
   required = ['cn']

   def __init__(self, cn=None, dn=None):
      self.dn = dn
      for k in self.__class__.attrmap.keys():
         self.__dict__[self.__class__.attrmap[k]] = None

   @classmethod
   def create(cls, connection):
      pass

   @classmethod
   def list(cls, connection, basedn):
      servers = []
      print "searching for %s" % cls.filter
      r = connection.search_s(basedn, ldap.SCOPE_SUBTREE, cls.filter)
      for entry in r:
          s = cls.fromldap(entry)
          servers.append(s)
      return s
   
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


   def ldif(self):
      s = []
      s.append("dn: " + self.dn)

      for oc in self.classes:
         s.append("objectClass: " + oc)

      for (class_name, attr_name) in self.__class__.attrmap.items():
         if self.__dict__[attr_name]:
            v = self.__dict__[attr_name]
            if type(v) == types.ListType:
               pass
            else:
               s.append(class_name + ": " + v)

      return "\n".join(s)
      
