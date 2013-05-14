import proxy
import referencecollection


class Repository(object):
    def __init__(self, path):
        if path:
            self._p_repo = proxy.git_repository_open(path)
        else:
            self._p_repo = None
        self._p_refs = None

    @property
    def is_bare(self):
        if self._p_repo is None:
            raise RuntimeError
        return proxy.git_repository_is_bare(self._p_repo)

    @property
    def head(self):
        if self._p_repo is None:
            raise RuntimeError
        self._ensureRefs()
        return self._p_refs['HEAD']

    def _ensureRefs(self):
        if not self._p_refs:
            self._p_refs = \
                referencecollection.ReferenceCollection(self._p_repo)
