

import module

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('sqlite:///example.db')

conn = engine.connect()

query = text("""
CREATE TABLE transaksi(
    id INT AUTO_INCTEMENT PRIMARY KEY,
    nama_item VARCHAR(100),
    jumlah_item INT,
    harga INT,
    total_harga INT
)
""")

conn.execute(query)
conn.close()
