'''
Fungsi      :   greeting 
Parameter   :   list data barang
Deskripsi   :   fungsi ini digunakan untuk menampilkan
                - selamat datang 
                - daftar barang promo 
                - dan menu utama
'''


def greet(databarang):
    print("""
  ****************************************************************
  *                 Selamat Datang di WARUNG SANCA               *
  ****************************************************************""")

   
    if len(databarang)>0:
        print("  *                        PROMO HARI INI                        *") 
        print("  ================================================================") 
        print("  *                                                              *") 
        for i in range(0,len(databarang)):
            harga = format(databarang[i]['harga'],',d').replace(',','.')
            print(f"  * PROMO !!! {databarang[i]['item']:^20}     HARGA PROMO --> {harga:>8}  *")
            if i < len(databarang)-1:
                print("  *--------------------------------------------------------------*")
            else:
                print("  *                                                              *") 
                print("  ****************************************************************") 

        print("""  *                 1. Beli Item PROMO                           *
  *                 2. All Item                                  *
  *                 X. Exit                                      *
  ****************************************************************""")
