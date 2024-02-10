

def hitung_faktorial(n: int) -> int:
    """
    Menghitung faktorial bilangan n menggunakan linear recursion.

    Args:
      n: bilangan n

    Returns:
      hasil faktorial n
    """

    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * hitung_faktorial(n - 1)


# 3. Panggil fungsi hitung_faktorial dengan parameter n yang telah diinputkan oleh pengguna.

hasil_hitung_faktorial: int = hitung_faktorial(n)

# 4. Cetak hasil perhitungan faktorial dengan format "{n}! = {hasil_hitung_faktorial}".

print(f"{n}! = {hasil_hitung_faktorial}.")
