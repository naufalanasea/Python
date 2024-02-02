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

#Cross: Membentuk salib putih di sisi atas.
#F2L: Menyelesaikan dua lapisan pertama (F2L) secara berpasangan.
#OLL: Mengorientasikan semua layer terakhir (OLL).
#PLL: Memposisikan semua layer terakhir (PLL).
