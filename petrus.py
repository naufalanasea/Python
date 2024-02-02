from rubik import Cube

# Algoritma Reduction
def reduction(cube):
  # ...

# Algoritma Edge Permutation
def edge_permutation(cube):
  # ...

# Algoritma Corner Permutation
def corner_permutation(cube):
  # ...

# Menyelesaikan kubus Rubik
cube = Cube()
reduction(cube)
edge_permutation(cube)
corner_permutation(cube)

# Verifikasi solusi
assert cube.is_solved()

#Reduction: Mengubah kubus ke state Petrus.
#Edge Permutation: Menyelesaikan permutasi edge.
#corner Permutation: Menyelesaikan permutasi corner.

