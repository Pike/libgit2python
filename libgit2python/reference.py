from . import proxy
from .core import ReferenceType
import binascii


class Reference(object):
    def __init__(self, canonicalName, targetIdentifier):
        self.canonicalName = canonicalName
        self.targetIdentifier = targetIdentifier

    def __repr__(self):
        return (self.canonicalName +
                ' -> ' +
                self.targetIdentifier)

    @staticmethod
    def buildFromPtr(ref_p, repo_p):
        _type = proxy.git_reference_type(ref_p)
        _name = proxy.git_reference_name(ref_p)
        print 'reference type', _type, _name
        if _type == ReferenceType.SYMBOLIC:
            targetIdentifier = proxy.git_reference_symbolic_target(ref_p)
            resolved = proxy.git_reference_resolve(ref_p)
            if not resolved:
                return SymbolicReference(_name, targetIdentifier, None)
            target_ref_p = Reference.buildFromPtr(resolved, repo_p)
            return SymbolicReference(_name, targetIdentifier,
                                     target_ref_p)
        elif _type == ReferenceType.OID:
            targetOid = proxy.git_reference_target(ref_p)
            return DirectReference(_name, repo_p,
                                   targetOid)


class SymbolicReference(Reference):
    def __init__(self, canonicalName, targetIdentifier, target):
        (super(SymbolicReference, self)
         .__init__(canonicalName, targetIdentifier))
        self.target = target

    def __repr__(self):
        return (super(SymbolicReference, self).__repr__() +
                ', ' +
                str(self.target))


class DirectReference(Reference):
    def __init__(self, canonicalName, repo, objectid):
        # XXX factor into a ObjectID wrapper
        sha = binascii.hexlify(objectid[0].id)
        (super(DirectReference, self)
         .__init__(canonicalName, sha))
        self._targetId = objectid
