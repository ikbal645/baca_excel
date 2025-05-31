import pandas as pd

# Baca file dan ambil 5 baris pertama
data = pd.read_excel('data_penjualan.xlsx').head()

# Tambahkan kolom Total Harga
data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']

# Simpan ke file baru
data.to_excel('5_baris_dengan_total.xlsx', index=False)

print("File '5_baris_dengan_total.xlsx' berhasil dibuat.")
