import proxy
from .reference import Reference


class ReferenceCollection(object):
    def __init__(self, proxyrepo):
        self._repo = proxyrepo

    def __getitem__(self, refname):
        return self.resolve(refname)

    def resolve(self, refname):
        ref_p = self._retrieveReference(refname, False)
        return ref_p and Reference.buildFromPtr(ref_p, self._repo) or None

    def _retrieveReference(self, refname, shouldRaise=True):
        ref_p = proxy.git_reference_lookup(self._repo, refname)
        return ref_p
