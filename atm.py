print("SELAMAT DATANG DI BANK SAT")
print("--------------------------")
print("Pilih Opsi : " )
print("1. Cek Saldo")
print("2. Tarik Saldo")
print("3. Nabung")
opsi = int(input("Masukan Opsi : "))
if opsi == 1:
  print("Uang anda berjumlah Rp. 1.500.000")

elif opsi == 2:
  print("Saldo anda berjumlah Rp. 1.500.000")
  print("Masukan nominal yang ingin ditarik : ")
  print("1. Rp. 100.000")
  print("2. Rp. 200.000")
  saldo = 1500000
  opsi2 = int(input("Pilih Opsi : "))
  if opsi2 == 1:
    hasil = saldo - 100000
    print("Saldo Anda sekarang Rp. ",hasil)
  elif opsi2 == 2:
    hasil2 = saldo - 200000
    print("Saldo anda sekarang Rp. ",hasil2)

  else :
    print("ATM ANDA DI BLOK")

elif opsi == 3:
  print("Masukan nominal yang anda ingin tabung : ")
  nominal = int(input("Nominal : "))
  hasil3 = nominal + 1500000
  print("Saldo anda sekarang Rp. ",hasil3)

else :
  print("GA ADA OPSI ITU JING")




