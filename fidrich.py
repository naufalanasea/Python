from rubik import Cube

# Algoritma Cross
def cross(cube):
  # ...

# Algoritma F2L
def f2l(cube):
  # ...

# Algoritma OLL
def oll(cube):
  # ...

# Algoritma PLL
def pll(cube):
  # ...

# Menyelesaikan kubus Rubik
cube = Cube()
cross(cube)
f2l(cube)
oll(cube)
pll(cube)

# Verifikasi solusi
assert cube.is_solved()
