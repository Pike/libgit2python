class ReferenceType:
    INVALID, OID, SYMBOLIC = range(3)
    LISTALL = OID | SYMBOLIC
