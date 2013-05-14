from libgit2python import repository
import sys

repo = repository.Repository(sys.argv[1])
print repo.head
