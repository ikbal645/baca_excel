import pandas as pd

# Baca file dan filter kategori Elektronik
data = pd.read_excel('data_penjualan.xlsx')
data_elektronik = data[data['Kategori'] == 'Elektronik'].head()

# Simpan ke file baru
data_elektronik.to_excel('elektronik_5_baris.xlsx', index=False)

print("File 'elektronik_5_baris.xlsx' berhasil dibuat.")