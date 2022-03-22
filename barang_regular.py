'''
Fungsi      :   daftar_regular
Parameter   :   list data barang dan data belanja
Deskripsi   :   fungsi ini digunakan untuk menampilkan
                daftar seluruh barang dan tempat dimana
                pelanggan membeli barang
'''
from barang_belanja import daftar_belanja


header_regular = """
  ****************************************************************
  *             Selamat Datang di Warung Sanca                   *
  ****************************************************************
  *                     DAFTAR ALL ITEM                          *
  ================================================================"""


def daftar_regular(databarang,databelanja):
    menu_regular = ""

    print(header_regular)
    for i in range(0,len(databarang)):
        harga = format(databarang[i]['harga'],',d').replace(',','.')
        print(f"  |{(i+1):>4} |{databarang[i]['item']:^30}     |     {harga:>8}  |")
        if i < len(databarang)-1:
            print("  ----------------------------------------------------------------")
        else:
            print("  ================================================================")
            print(f"  *         Silahkan pilih no. 1 ... {len(databarang):<4}                        *")
            print("  *         Atau tekan X bila selesai belanja                    *")
            print("  ****************************************************************")
    
    pilihan = [str(num) for num in range(1,len(databarang)+1)]
    pilihan.append('x')


    while True:
        indexbarang = None
        jumlahbarang = 0
        item_belanja = {}
        while menu_regular.lower() not in pilihan:
            menu_regular = input("  Pilih barang no. ? ")
        
        if menu_regular.lower() != 'x':
            indexbarang = int(menu_regular) - 1
            while True:
                try:
                    jumlahbarang = int(input(f"  {databarang[indexbarang]['item']}, jumlah = "))
                    break
                except ValueError:
                    print("Jumlah harus angka !")

            item_belanja['item'] = databarang[indexbarang]['item']
            item_belanja['harga'] = databarang[indexbarang]['harga']
            item_belanja['jumlah'] = jumlahbarang
            item_belanja['total'] = databarang[indexbarang]['harga']*jumlahbarang
            databelanja.append(item_belanja)
            menu_regular =""
        else:
            daftar_belanja(databelanja)
            input("Tekan Enter untuk melanjutkan...")

            break
    
