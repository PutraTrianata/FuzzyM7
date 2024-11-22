import numpy as np


def pendapatan_rendah(x):
    return max(0, (3 - x) / 3) if x < 3 else 0

def pendapatan_sedang(x):
    if 3 <= x <= 10:
        return min((x - 3) / 7, (10 - x) / 7)
    return 0

def pendapatan_tinggi(x):
    return max(0, (x - 10) / 5) if x > 10 else 0

def hutang_sedikit(x):
    return max(0, (5 - x) / 5) if x <= 5 else 0

def hutang_sedang(x):
    if 5 <= x <= 15:
        return min((x - 5) / 10, (15 - x) / 10)
    return 0

def hutang_banyak(x):
    return max(0, (x - 15) / 10) if x > 15 else 0

def usia_muda(x):
    return max(0, (25 - x) / 25) if x <= 25 else 0

def usia_paruh_baya(x):
    if 25 <= x <= 50:
        return min((x - 25) / 25, (50 - x) / 25)
    return 0

def usia_tua(x):
    return max(0, (x - 50) / 25) if x > 50 else 0

# Aturan fuzzy
def inferensi(pendapatan, hutang, usia):
    """
    Menghasilkan daftar aturan fuzzy aktif dengan nilai derajat keanggotaan (μ) dan output crisp (z).
    """
    rules = []

    rules.append((
        min(pendapatan_tinggi(pendapatan), hutang_sedikit(hutang), usia_paruh_baya(usia)),
        90
    ))

    rules.append((
        min(pendapatan_rendah(pendapatan), hutang_banyak(hutang), usia_tua(usia)),
        30
    ))

    rules.append((
        min(pendapatan_sedang(pendapatan), hutang_sedang(hutang), usia_muda(usia)),
        70
    ))

    rules.append((
        min(pendapatan_sedang(pendapatan), hutang_sedang(hutang), usia_paruh_baya(usia)),
        60
    ))

    rules.append((
        min(pendapatan_tinggi(pendapatan), hutang_sedang(hutang)),
        85
    ))

    rules.append((
        min(pendapatan_rendah(pendapatan), hutang_sedikit(hutang)),
        50
    ))

    return rules

# Defuzzifikasi
def defuzzifikasi(rules):
    """
    Melakukan defuzzifikasi menggunakan Weighted Average Method.
    """
    numerator = sum(mu * z for mu, z in rules)
    denominator = sum(mu for mu, _ in rules)
    return numerator / denominator if denominator != 0 else 50


print("Masukkan data calon debitur:")
pendapatan = float(input("Pendapatan (dalam juta rupiah): "))
hutang = float(input("Hutang (dalam juta rupiah): "))
usia = float(input("Usia (dalam tahun): "))

# Proses inferensi dan defuzzifikasi
rules = inferensi(pendapatan, hutang, usia)
kelayakan = defuzzifikasi(rules)

print(f"\nData Calon Debitur:")
print(f"- Pendapatan: {pendapatan} juta")
print(f"- Hutang: {hutang} juta")
print(f"- Usia: {usia} tahun")
print(f"\nHasil Kelayakan Kredit: {kelayakan:.2f}")
