# ASN Lookup Service

Uses the DNS-based service by
(http://www.team-cymru.org/IP-ASN-mapping.html)[Team Cymru] to collect information about
Autonomous Service Numbers used in BGP.

For each ASN it will execute the following DNS query against the local
DNS resolver

```
dig TXT as<ASN>.asn.cymru.com
```

## Installation

```
python setup.py install
```

## Requirements

* Twisted

## Usage

```
from asn_name_lookup import AsnNameLookupService

s = AsnNameLookupService()
print s.lookup_many(["133029", "20912", "9500", "3557"])
```

For each ASN queried it will provide a dictionary with the ASN as key,
and value a dictionary with country, a short description, and a long description
