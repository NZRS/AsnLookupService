__author__ = 'secastro'


from asn_name_lookup import AsnNameLookupService

s = AsnNameLookupService()
print s.lookup_many(["133029", "20912", "65154", "3557"])
