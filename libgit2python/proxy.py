from ctypes import cdll, Structure, POINTER, byref, c_char_p, c_byte

libgit2 = cdll.LoadLibrary('libgit2.dylib')

class Repository(Structure):
    _fields_ = []

class Reference(Structure):
    _fields_ = []

class Oid(Structure):
    _fields_ = [
        ('id', c_byte*20)
        ]

def git_repository_open(path):
    repo_p = POINTER(Repository)()
    rv = libgit2.git_repository_open(byref(repo_p), path)
    return repo_p


def git_repository_is_bare(repo):
    return bool(libgit2.git_repository_is_bare(repo))


def git_reference_lookup(repo, name):
    ref_p = POINTER(Reference)()
    rv = libgit2.git_reference_lookup(byref(ref_p), repo, name)
    return ref_p


libgit2.git_reference_name.restype = c_char_p
def git_reference_name(ref_p):
    return libgit2.git_reference_name(ref_p)


def git_reference_type(ref_p):
    return libgit2.git_reference_type(ref_p)


libgit2.git_reference_target.restype = POINTER(Oid)
def git_reference_target(ref_p):
    return libgit2.git_reference_target(ref_p)


def git_reference_resolve(ref_p):
    resolved_ref_p = POINTER(Reference)()
    rv = libgit2.git_reference_resolve(byref(resolved_ref_p), ref_p)
    return resolved_ref_p


libgit2.git_reference_symbolic_target.restype = c_char_p
def git_reference_symbolic_target(ref_p):
    return libgit2.git_reference_symbolic_target(ref_p)
