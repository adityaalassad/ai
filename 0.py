jenis_tiket = str(input("MASUKAN JENIS TIKET = "))
waktu_tiket = str(input("MASUKAN WAKTU TIKET = "))
jumlah_tiket = int(input("MASUKAN JUMLAH TIKET = "))
Print("=" * 40)
if jenis_tiket == "ekonomi":
    if waktu_tiket == "pagi":
        harga = 20000
    elif waktu_tiket == "malam":
        harga = 50000
    else waktu_tiket == 0:
        harga = 0

