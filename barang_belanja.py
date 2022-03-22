'''
Fungsi      :   daftar_belanja 
Parameter   :   list data belanja
Deskripsi   :   fungsi ini digunakan untuk menampilkan
                daftar barang yang sudah dibeli oleh
                konsumen, dimana tercantum nilai total
                yang harus dibayarnya.
'''

def daftar_belanja(databelanjaan):
    header_belanjaan = '''
    ****************************************************************
    *                 Selamat Datang di WARUNG SANCA               *
    ****************************************************************'''
    header_belanjaan2 ='''    *                 DAFTAR BELANJA ANDA SAAT INI                 *
    ================================================================
    |  No  |       Nama Barang    | Harga    |  Qty |   Total      |
    |==============================================================|
    |      |                      |          |      |              |'''
    footer_belanjaan =  '''    |==============================================================|'''
    footer_belanjaan2 = '''    |--------------------------------------------------------------|'''
    footer_belanjaan3 = '''    |        Terima kasih sudah berbelanja di WARUNG SANCA         |'''
    footer_belanjaan4 = '''    |______________________________________________________________|'''
    print(header_belanjaan)

    if len(databelanjaan) > 0:
        print(header_belanjaan2)
        total_bayar = 0
        for i in range(0,len(databelanjaan)):
            harga = format(databelanjaan[i]['harga'],',d').replace(',','.')
            total = format(databelanjaan[i]['total'],',d').replace(',','.')
            print(f"    | {i+1:>4} | {databelanjaan[i]['item']:^20} | {harga:>8} | {databelanjaan[i]['jumlah']:>4} | {total:>8}     |")
            total_bayar += databelanjaan[i]['total']
        print(footer_belanjaan)
        print(f"    |                               Total Bayar     | {format(total_bayar,',d').replace(',','.'):>8}     |")
        print(footer_belanjaan)
        print(footer_belanjaan3)
        print(footer_belanjaan4)