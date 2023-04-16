import pandas as pd
import os


items = []
jumlah_items = []
items_price = []
total_harga = []

class Transaction(object):

    def __init__(self):
        pass

    def main(self):
        """
        Fungsi Untuk menampilkan daftar Tugas
        """

        dataOrder = ("""==============================================
        1. Tambah Data Transaksi
        2. Ubah Data item order
        3. Ubah Jumlah item order
        4. Ubah harga per item
        5. Check Order
        6. Hapus Salah Satu Order
        7. Hapus Semua data transaksi
        8. Tampilkan Total Harga Transaksi
        9. Keluar

        Opsi Pilihan : """)

        welcome = "Welcome to SUPER CASHIER"

        while (user_input := input(dataOrder)) != "9":
            if user_input == "1":
                self.add_item() # Done
            elif user_input == "2":
                self.update_item_name() # Done
            elif user_input == "3":
                self.update_item_qty()
            elif user_input == "4":
                self.update_item_price()
            elif user_input == "5":
                self.check_order_item # Done
            elif user_input == "6":
                self.delete_item() # Done
            elif user_input == "7":
                self.reset_transaction() # Done
            elif user_input == "8":
                self.total_price()
            elif user_input == "9":
                break                
            else:
                print("Tolong Masukan Nomer Opsi yang Benar")

    def add_item(self):

        self.nama_item = input("Nama Item : ")

        while True:
            try:
                self.jumlah_item = int(input("Jumlah Barang : "))
                try:
                    if self.jumlah_item < 0 :
                        print("Masukan Angka Positive")
                except ValueError:
                    print("Masukan input berupa Angka!")

                break
            except ValueError:
                print("Masukan input berupa Angka!")
                continue

        while True:
            try:
                self.harga = int(input("Harga : "))
                try:
                    if self.harga < 0 :
                        print("Masukan Angka Positive")
                except ValueError:
                    print("Masukan input berupa Angka!")
                break
            except ValueError:
                print("Masukan input berupa Angka!")
                continue
        
        self.jumlah_harga = self.jumlah_item* self.harga

        items.append(self.nama_item)
        jumlah_items.append(self.jumlah_item)
        items_price.append(self.harga)
        total_harga.append(self.jumlah_harga)

        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}          
        tabel_transaksi = pd.DataFrame(dict_transaksi)    
        print(tabel_transaksi)


    def update_item_name(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}

        nama_item = input("Nama Item yang yang ingin Diubah: ")
        if nama_item in dict_transaksi.get('Pesanan'):
            update_nama_item = input("Update nama item yang akan diubah: ")
            index_item = dict_transaksi['Pesanan'].index(nama_item)
            dict_transaksi['Pesanan'][index_item] = update_nama_item
            print("Berhasil Berubah")
        else:
            print("Ups, tidak ada nama item itu.")

    def update_item_qty(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}
        while True:
            nama_item = input("Nama Item yang jumlahnya ingin diganti: ")
            if nama_item in dict_transaksi.get("Pesanan"):
                while True:
                    try:
                        update_jumlah_item = int(input("jumlah item Pesanan yang akan diubah: "))
                    except ValueError:
                        print("Input berupa angka!")
                        continue
                index_item = dict_transaksi['Pesanan'].index(nama_item)
                dict_transaksi['Jumlahan Pesanan'][index_item] = update_jumlah_item

                dict_transaksi['Jumlah Pesanan'][index_item] = (
                    update_jumlah_item * dict_transaksi["Harga Pesanan"][index_item]
                )
                print("Berhasil dirubah")
                break
            else:
                print("Tidak terdapat nama Pesanan")

    def update_item_price(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}
        while True:                          
            nama_item = input("Nama Item yang jumlahnya ingin diganti: ")
            if nama_item in dict_transaksi.get("Pesanan"):
                while True:
                    try:
                        update_harga_item = int(input("jumlah item harga yang akan diubah: "))
                    except ValueError:
                        print("Input berupa angka!")
                        continue
                index_item = dict_transaksi['esanan'].index(nama_item)
                dict_transaksi['Harga Pesanan'][index_item] = update_harga_item
                dict_transaksi['Total Pembayaran'][index_item] = (
                    update_harga_item * dict_transaksi["Jumlah Pesanan"][index_item])
                print("Berhasil dirubah")
                break
            else:
                    print("Tidak terdapat nama Pesanan")

            



    def check_order_item(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}
        if not any(dict_transaksi.values()):
          print("Tidak ada data transaksi!")
        else:
            print("Data transaksi sudah benar!")
            print("<--------List order item-------->")
            df = pd.DataFrame(dict_transaksi)
            print(df)

        from sqlalchemy import create_engine
        from sqlalchemy import text

        engine = create_engine('sqlite:///example.db')

        conn = engine.connect()


        query = text("""
        INSERT INTO transaksi(nama_item, jumlah_item, harga, total_harga)
        VALUES (:nama_item, :jumlah_item, :harga, :total_harga)
        )
        """)

        conn.execute(query,
        nama_item = dict_transaksi["Pesanan"],
        jumlah_item = dict_transaksi["Jumlah Pesanan"],
        harga = dict_transaksi["Harga Pesanan"],
        total_harga = dict_transaksi["Total Pembayaran"],)
        conn.close()


    def delete_item(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}
        while True:
            nama_item = input("Nama Item yang akan Dihapus: ")
            if nama_item in dict_transaksi.get("Pesanan"):
                idx_item = dict_transaksi['Pesanan'].index(nama_item)
                for key in list(dict_transaksi.keys()):
                    del dict_transaksi[key][idx_item]
                    print("Data Berhasil dihapus")
                if not any(dict_transaksi.values()):
                    print("Tidak ada data transaksi")
                else:
                    df = pd.DataFrame(dict_transaksi)
                    print(df)
                    break
            else:
                print("Tidak terdapat nama item tersebut")

    def reset_transaction(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}
        for key in list(dict_transaksi.keys()):
            del dict_transaksi[key][:]
        
        print("Semua Data Transaksi sudah di hapus")



    def total_price(self):
        dict_transaksi = {'Pesanan' : items,
                          'Jumlah Pesanan':jumlah_items,
                          'Harga Pesanan':items_price, 
                          'Total Pembayaran' : total_harga}

        if not any(dict_transaksi.values()):
          print("Tidak ada data transaksi!")
        else:
            df = pd.DataFrame(dict_transaksi)
            print(df)
            if sum(dict_transaksi["Total Pembayaran"]) > 500000:
                print("Sebelum mendapatkan diskon 7%: Rp.{}".format(sum(dict_transaksi["Total Pembayaran"])))
                print("Setelah mendapatkan diskon 7%: Rp.{}".format(
                    int(sum(dict_transaksi["Total Pembayaran"]) - (sum(dict_transaksi["Total Pembayaran"]) * 0.07))))
            elif sum(dict_transaksi["Total Pembayaran"]) > 300000:
                print("Sebelum mendapatkan diskon 6%: Rp.{}".format(sum(dict_transaksi["Total Pembayaran"])))
                print("Setelah mendapatkan diskon 6%: Rp.{}".format(
                    sum(int(dict_transaksi["Total Pembayaran"]) - (sum(dict_transaksi["Total Pembayaran"]) * 0.06))))
            elif sum(dict_transaksi["Total Pembayaran"]) > 200000:
                print("Sebelum mendapatkan diskon 5%: Rp.{}".format(sum(dict_transaksi["Total Pembayaran"])))
                print("Setelah mendapatkan diskon 5%: Rp.{}".format(
                    sum(int(dict_transaksi['Total Pembayaran']) - (sum(dict_transaksi["Total Pembayaran"]) * 0.05))))
