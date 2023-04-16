
 ## Background Project
 
 
 Andi  adalah  seorang  pemilik  supermarket  besar  di  salah  satu  kota  di  Indonesia.  Andi  memiliki 
 rencana  untuk  melakukan  perbaikan  proses  bisnis,  yaitu  Andi  akan  membuat  sistem  kasir  yang 
 self-service di supermarket miliknya dengan harapan 
 ●  Customer  bisa  langsung  memasukkan  item  yang  dibeli,  jumlah  item  yang  dibeli,  dan 
 harga item yang dibeli dan fitur yang lain. 
 ●  Customer  yang  tidak  berada  di  kota  tersebut  bisa  membeli  barang  dari  supermarket 
 tersebut. 
 
Setelah  Andi  melakukan  riset,  ternyata  Andi  memiliki  masalah,  yaitu  Andi  membutuhkan 
 Programmer  untuk  membuatkan  fitur  -  fitur  agar  sistem  kasir  self-service  di  supermarket  itu  bisa 
 berjalan dengan lancar. 
 
 
 ## Feature Requirements 

1.  Customer membuat ID transaksi customer berikut 
 a.  Dengan membuat objek dari function :  trnsct_123 =  transaction() 
 
2.  Kemudian, Customer memasukkan nama item, jumlah item, dan harga barang. 
 a.  Masukkan item yang ingin dibeli. 
 add_item([<nama item>, <jumlah item>, <harga per item>]) 
 
3.  Jika ternyata ada kesalahan dalam memasukkan nama item atau jumlah item atau 
 harga item tetapi tidak ingin menghapus itemnya, Customer bisa melakukan 
 a.  Update nama item dengan method: 
 update_item_name(<nama item>, <update nama item>) 
 b.  Update jumlah item dengan method: 
 update_item_qty(<nama_item>, <update jumlah item>) 
 c.  Update harga item menggunakan method: 
 update_item_price(<nama_item>, <update harga item>) 
 
4.  Jika batal membeli item belanjaan, Customer bisa melakukan 
 a.  Menghapus salah satu item dari nama item dengan method 
 delete_item(<nama item>)
 Ketika menghapus salah satu nama item, maka jumlah item dan harga per item 
 pada baris/list tersebut akan ikut terhapus 
 b.  Langsung menghapus semua transaksi atau reset transaksi dengan method 
 reset_transaction() 
 
5.  Customer sudah selesai dengan berbelanja online nya, tetapi Customer masih ragu 
 apakah harga barang dan nama barang yang diinput sudah benar. Bisa saja Customer 
 melakukan kesalahan dalam melakukan input, semisal sudah melakukan input harga 
 barang tetapi lupa untuk input nama barangnya. Andi bisa menggunakan method 
 check_order().  Terdapat ketentuan: 
 a.  Akan mengeluarkan pesan  “Pemesanan sudah benar”  (bebas  bisa dengan 
 message yang lain)  jika tidak ada kesalahan input 
 b.  Akan mengeluarkan pesan  “Terdapat kesalahan input  data”  jika terjadi 
 kesalahan input 
 c.  Keluarkan output transaksi atau pemesanan apa saja yang sudah dibeli. 
 Contoh Output: 
 | No | Nama Item | Jumlah Item | Harga/Item | Total Harga | 
 |----|-----------|-------------|------------|-------------| 
 | 1  | Mobil     | 2           | 100000     | 200000      | 
 | 2  | Mie       | 1           | 5000       | 5000        | 
 | 3  | Tempe     | 3           | 3000       | 9000        | 
 
6.  Setelah melakukan pengecekan, Customer bisa menghitung total belanja yang sudah 
 dibeli. Andi bisa menggunakan method  check_out() 
 .  Pada supermarket ini ternyata 
 terdapat ketentuan: 
 a.  Jika  total  harga  per  item  Andi  diatas  Rp  200.000  maka  akan  mendapatkan 
 diskon 5% 
 b.  Jika  total  harga  per  item  Andi  diatas  Rp  300.000  maka  akan  mendapatkan 
 diskon 6% 
 c.  Jika  total  harga  per  item  Andi  diatas  Rp  500.000  maka  akan  mendapatkan 
 diskon 7% 
 d.  Total  pembelian  hanya  ditampilkan  pada  method  check_out() namun  tidak  di 
 simpan di dalam database 
