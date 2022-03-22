from greeting import greet
from barang_promo import daftar_promo
from barang_regular import daftar_regular
from barang_belanja import daftar_belanja

data_barang = []
data_belanja = []

all_items = [   { "item": "susu", "harga": 50000 }, {"item": "daging", "harga": 20000} , 
                {"item": "lampu","harga": 15000} , {"item": "masker", "harga": 25000}, 
                {"item": "apel", "harga": 30000} ]

promotional_items = [ { "item": "susu", "harga": 50000 }, {"item": "masker", "harga": 25000} ]


while True:
    greet(promotional_items)
    
    menu =""
    while menu not in ["1","2","x","X"]:
        menu = input("   Pilihan anda ? ( 1 atau 2 atau Tekan X untuk keluar..) ")


    if menu == "1":
        daftar_promo(promotional_items,data_belanja)
    elif menu == "2":
        daftar_regular(all_items,data_belanja)
    else:
        break


