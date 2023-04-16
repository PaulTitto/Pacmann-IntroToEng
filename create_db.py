# no_id : nomer id (auto increment)
# ii. nama_item : nama barang yang dibeli
# iii. jumlah_item : jumlah barang yang dibeli
# iv. harga : harga barang
# v. total_harga : total harga (jumlah item * harga)
# vi. diskon : potongan harga
# vii. harga_diskon

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('sqlite://example.db')

conn = engine.connect()

query = text("""
CRAETE TABLE transaction (
    no_id INT AUTO_INCTEMENT PRIMARY KEY,
    nama_item VARCHAR(100),
    jumlah_item INT,
    harga INT,
    total_harga INT,
    diskon FLOAT,
    harga_diskon FLOAT
)
""")

conn.execute(query)
conn.close()
