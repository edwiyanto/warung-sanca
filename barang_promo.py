'''
Fungsi      :   daftar_promo 
Parameter   :   list data barang dan data belanja
Deskripsi   :   fungsi ini digunakan untuk menampilkan
                daftar barang PROMO, dan juga tempat 
                pelanggan berbelanja.
'''

from barang_belanja import daftar_belanja

header_promo = """ 
  *********************************************************************
  *                Selamat Datang di WARUNG SANCA                     *
  *********************************************************************
  *                     PROMO HARI INI                                *
  ====================================================================="""


def daftar_promo(databarang,databelanja):
    menu_promo = ""
    
    print(header_promo)

    for i in range(0,len(databarang)):
        harga = format(databarang[i]['harga'],',d').replace(',','.')
        print(f"  |{(i+1):>4} |{databarang[i]['item']:^30} HARGA PROMO -->     {harga:>8}  |")
        if i < len(databarang)-1:
            print("  ---------------------------------------------------------------------")
        else:
            print("  =====================================================================")
            print(f"  *                Silahkan pilih no. 1 ... {len(databarang):<4}                      *")
            print("  *             Atau tekan X bila selesai belanja                     *")
            print("  *********************************************************************")

    pilihan = [str(num) for num in range(1,len(databarang)+1)]
    pilihan.append('x')

    while True:
        indexbarang = None
        jumlahbarang = 0
        item_belanja = {}
        while menu_promo.lower() not in pilihan:
            menu_promo = input("  Pilih barang no. ? ")
        
        if menu_promo.lower() != 'x':
            indexbarang = int(menu_promo) - 1
            while True:
                try:
                    jumlahbarang = int(input(f"  --> {databarang[indexbarang]['item']} ,jumlah = "))
                    break
                except ValueError:
                    print("Jumlah harus angka !")

            item_belanja['item'] = databarang[indexbarang]['item']
            item_belanja['harga'] = databarang[indexbarang]['harga']
            item_belanja['jumlah'] = jumlahbarang
            item_belanja['total'] = databarang[indexbarang]['harga']*jumlahbarang
            databelanja.append(item_belanja)
            menu_promo =""
        else:
            daftar_belanja(databelanja)
            input("Tekan Enter untuk melanjutkan...")

            break
    
