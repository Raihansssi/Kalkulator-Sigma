print("Kalkulator Sigma")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
pilihan = input("Pilih (1/2/3/4): ")
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))
if pilihan == "1":
 hasil = a + b
elif pilihan == "2":
 hasil = a - b
elif pilihan == "3":
 hasil = a * b
elif pilihan == "4":
    if b == 0:
        hasil = "gabisa dibagi nol"
    else:
        hasil = a / b
else:
    hasil = "pilihan salah"

print("Hasil:", hasil)
